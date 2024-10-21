import os, string, random, json
import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .serializers import CSVUploadSerializer, CSVProcessorSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.sessions.models import Session

from pprint import pp 

@login_required(login_url="/users/signin/")
def csv_processor(request):
    context = {
        'segment': 'csv_processor',
        'parent': 'tools'
    }
    return render(request, "tools/csv-processor.html", context)

def generate_random_string(length=5):
    """Generate a random string of fixed length."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(random.choice(characters) for _ in range(length))

class CSVUploadView(APIView):

    def post(self, request, *args, **kwargs):
        # Check for sessionid in cookies
        sessionid = self._get_sessionid(request)
        if not sessionid:
            return self._unauthorized_response()

        session = Session.objects.get(session_key=sessionid)
        session_data = session.get_decoded()
        user_id = session_data.get("_auth_user_id")
        if not user_id:
            return self._unauthorized_response()

        # Validate and serialize the file input
        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            return self._handle_file_upload(serializer, user_id)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """Retrieve all files uploaded by the current user"""
        sessionid = self._get_sessionid(request)

        # Check if session ID is present
        if not sessionid:
            return self._unauthorized_response()

        try:
            session = Session.objects.get(session_key=sessionid)
            session_data = session.get_decoded()
            user_id = session_data.get("_auth_user_id")
            if not user_id:
                return self._unauthorized_response()

            return self._retrieve_user_files(user_id)

        except Session.DoesNotExist:
            return Response(
                {"detail": "Session not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def _get_sessionid(self, request):
        return request.COOKIES.get("sessionid")

    def _unauthorized_response(self):
        return Response(
            {"detail": "Unauthorized User. Please login first"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def _handle_file_upload(self, serializer, user_id):
        file = serializer.validated_data["file"]
        upload_path = self._create_user_directory(user_id)

        # Generate a random 5-character string for the filename
        random_string = generate_random_string()
        file_extension = os.path.splitext(file.name)[1]
        file_name = os.path.splitext(file.name)[0]

        # Create a new filename with the random string
        new_filename = f"{file_name}_{random_string}{file_extension}"
        file_path = os.path.join(upload_path, new_filename)

        # Save the file
        saved_file_name = default_storage.save(file_path, ContentFile(file.read()))

        return Response(
            {
                "message": "CSV file uploaded successfully",
                "file_path": os.path.join(settings.MEDIA_URL, saved_file_name),
            },
            status=status.HTTP_201_CREATED,
        )

    def _create_user_directory(self, user_id):
        upload_path = os.path.join("user-{}/csv/".format(user_id))
        full_path = os.path.join(settings.MEDIA_ROOT, upload_path)

        # Ensure the directory exists
        os.makedirs(full_path, exist_ok=True)
        return upload_path

    def _retrieve_user_files(self, user_id):
        upload_path = os.path.join(f"user-{user_id}/csv/")
        full_path = os.path.join(settings.MEDIA_ROOT, upload_path)

        # Check if the directory exists and list files
        if os.path.exists(full_path):
            files = os.listdir(full_path)
            if files:
                file_paths = [
                    os.path.join(settings.MEDIA_URL, upload_path, file)
                    for file in files
                ]
                return Response(
                    {"message": "Files retrieved successfully", "files": file_paths},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"message": "No files found for the current user."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {"message": "User has not uploaded any files."},
            status=status.HTTP_404_NOT_FOUND,
        )

@method_decorator(login_required(login_url="/users/signin/"), name="dispatch")
class CSVProcessorView(APIView):
    def post(self, request, *args, **kwargs):
        # Check for sessionid in cookies
        sessionid = request.COOKIES.get("sessionid")
        if not sessionid:
            return self.unauthorized_response()

        try:
            serializer = CSVProcessorSerializer(data=request.data)

            if serializer.is_valid():
                pp ( request.data )
                print( ' > file: ' + request.data['file'])
                
                relative_file_path = request.data['file']
                fields = request.data['fields']

                if relative_file_path.startswith('/media/'):
                    relative_file_path = relative_file_path.replace('/media/', '', 1)

                file_path = os.path.join(settings.MEDIA_ROOT, relative_file_path)

                self.process_csv(file_path, fields)
                return self.success_response(serializer.data["file"])

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return self.error_response(e)
    

    def process_csv(self, file_path, fields):
        df = pd.read_csv(file_path)

        for column, properties in fields.items():
            if column in df.columns:
                if properties.get('transformer') == 'delete':
                    df.drop(column, axis=1, inplace=True)
                elif properties.get('transformer') == 'uppercase':
                    df.rename(columns={column: column.upper()}, inplace=True)
                elif properties.get('new_name'):
                    df.rename(columns={column: properties['new_name']}, inplace=True)

        df.to_csv(file_path, index=False)

    def unauthorized_response(self):
        return Response(
            {"detail": "Unauthorized User. Please login first"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    def success_response(self, file_path):
        return Response(
            {
                "message": "Processed file",
                "file_path": file_path,
            },
            status=status.HTTP_200_OK,
        )

    def error_response(self, error):
        return Response(
            {"detail": f"An error occurred during processing {str(error)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
