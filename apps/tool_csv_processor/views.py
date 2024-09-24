from django.shortcuts import render
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .serializers import CSVUploadSerializer, CSVProcessorSerializer
import random
import string


def csv_processor(request):
    return render(request, "tools/csv-processor.html")


def generate_random_string(length=5):
    """Generate a random string of fixed length."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return "".join(random.choice(characters) for _ in range(length))


class CSVUploadView(APIView):

    def post(self, request, *args, **kwargs):
        # Check for session_id in cookies
        session_id = self._get_session_id(request)
        if not session_id:
            return self._unauthorized_response()

        # Validate and serialize the file input
        serializer = CSVUploadSerializer(data=request.data)

        if serializer.is_valid():
            return self._handle_file_upload(serializer, request.user.id)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """Retrieve all files uploaded by the current user"""
        session_id = self._get_session_id(request)
        if not session_id:
            return self._unauthorized_response()

        user_id = request.user.id
        return self._retrieve_user_files(user_id)

    def _get_session_id(self, request):
        return request.COOKIES.get("session_id")

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


class CSVProcessorView(APIView):
    def post(self, request, *args, **kwargs):
        # Check for session_id in cookies
        session_id = request.COOKIES.get("session_id")
        if not session_id:
            return self.unauthorized_response()

        try:
            serializer = CSVProcessorSerializer(data=request.data)

            if serializer.is_valid():
                return self.success_response(serializer.data["file"])

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return self.error_response(e)

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
