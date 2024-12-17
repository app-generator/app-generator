from django.utils.deprecation import MiddlewareMixin
from apps.common.models import Event, EventType
import json

class APILoggingMiddleware(MiddlewareMixin):

    def process_request(self, request):
    
        if request.path.startswith('/api/') and request.method in ['POST', 'PUT', 'PATCH']:
            try:
                request.body_data = json.loads(request.body.decode('utf-8')) if request.body else None
            except json.JSONDecodeError:
                request.body_data = None
        else:
            request.body_data = request.GET.dict()

    def process_response(self, request, response):
        try:
            if request.path.startswith('/api/'):
                user = request.user if hasattr(request, 'user') and request.user.is_authenticated else None
                endpoint = request.get_full_path()
                input_data = getattr(request, 'body_data', None)
                output_data = response.data if hasattr(response, 'data') else response.content

                if not isinstance(input_data, str):
                    input_data = json.dumps(input_data)
                if not isinstance(output_data, str):
                    output_data = json.dumps(output_data)

                Event.objects.create(
                    userId=user.id if user else -1,
                    type=EventType.API,
                    text=endpoint,
                    input=json.loads(input_data) if input_data else None,
                    output=json.loads(output_data) if output_data else None,
                    status_code=response.status_code,
                )
        except Exception as e:
            print(f"Logging error: {e}")

        return response

    def process_exception(self, request, exception):
        try:
            if request.path.startswith('/api/'):
                user = request.user if hasattr(request, 'user') and request.user.is_authenticated else None
                endpoint = request.get_full_path()
                input_data = getattr(request, 'body_data', None)
                output_data = {"error": str(exception)}

                if not isinstance(input_data, str):
                    input_data = json.dumps(input_data)

                Event.objects.create(
                    userId=user.id if user else -1,
                    type=EventType.API,
                    text=endpoint,
                    input=json.loads(input_data) if input_data else None,
                    output=output_data,
                    status_code=500,
                )
        except Exception as e:
            print(f"Logging exception error: {e}")
