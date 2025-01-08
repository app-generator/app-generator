from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserDetailsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        output_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        response = Response(output_data)
        return response
        


# Generate project API

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

from apps.common.models import *
from helpers.generator import *
from helpers.util import get_client_ip

from apps.tasks.tasks import *
from apps.common.models_generator import *
from django.utils.timezone import now
from datetime import timedelta

# LOGGER & Events
from helpers.logger import *
from helpers.events import *

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.utils.timezone import now
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

class StatusViewAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logger
        func_name = sys._getframe().f_code.co_name
        logger.info(f'[{__name__}->{func_name}()] Begin')

        user = request.user  # Get authenticated user
        user_ip = get_client_ip(request)

        # Restrict unauthenticated users to one request per hour (Token handles authentication now)
        one_hour_ago = now() - timedelta(hours=1)
        recent_app = GeneratedApp.objects.filter(user_ip=user_ip, generated_at__gte=one_hour_ago).first()

        if not user and recent_app:
            return Response(
                {"status": "429", "info": "Please Sign In or try again in one hour."},
                status=status.HTTP_429_TOO_MANY_REQUESTS,
            )

        try:
            # Create the task
            result = task_generator.delay(request.data)
            app = GeneratedApp()
            app.task_id = result.id
            app.user_ip = user_ip
            app.user = user if user.is_authenticated else None

            # Save the creation
            request_data = (
                request.data.decode('utf-8') if isinstance(request.data, bytes) else request.data
            )
            app.task_log = json.dumps(request_data)
            app.save()

            logger.info(f'[{__name__}->{func_name}()] Task created with ID: {result.id}')
            task_result = result.get()

            logger.info(f'[{__name__}->{func_name}()] Task result: {task_result.get("task_result", "NA_task_result")}')
            app.task_log = json.dumps(task_result)
            app.task_state = task_result.get('task_state', 'NA_task_state')
            app.task_result = task_result.get('task_result', 'NA_task_result')

            if "gh_repo" in task_result:
                app.gh_repo = task_result.get('gh_repo', 'NA_gh_repo')

            app.save()

            task_result["status"] = (
                task_result.get('task_state', 'NA_task_state') + ", " + task_result.get('task_result', 'NA_task_result')
            )
            task_result["info"] = (
                task_result.get('task_info', 'NA_task_info') + ", result: " + task_result.get('task_output', 'NA_task_output')
            )

            logger.info(f'[{__name__}->{func_name}()] End')
            return Response(task_result, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f'[{__name__}->{func_name}()] Error: {e}')
            return Response(
                {"status": "500", "info": f"Task exited with error: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
