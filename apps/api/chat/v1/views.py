from apps.api.chat.v1.serializers import ChatSerializer
from apps.api.product.v1.serializers import ProductSerializer
from apps.common.models import Products, Type
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from difflib import get_close_matches


class ChatView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.data['prompt'].strip().lower()
            options = ['dashboard', 'app', 'api', 'dash']

            if prompt == 'help':
                return Response({'response': "Type `dashboard`, `app` or `api` to display products.", 'type': 'help'}, status=status.HTTP_200_OK)
            elif 'dash' in prompt:
                products = Products.objects.filter(type=Type.DASHBOARD)
                product_serializer = ProductSerializer(products, many=True)
                return Response({'response': product_serializer.data, 'type': 'products'}, status=status.HTTP_200_OK)
            elif 'app' in prompt:
                products = Products.objects.filter(type=Type.WEBAPP)
                product_serializer = ProductSerializer(products, many=True)
                return Response({'response': product_serializer.data, 'type': 'products'}, status=status.HTTP_200_OK)
            elif 'api' in prompt:
                products = Products.objects.filter(type=Type.API)
                product_serializer = ProductSerializer(products, many=True)
                return Response({'response': product_serializer.data, 'type': 'products'}, status=status.HTTP_200_OK)
            else:
                closest_matches = get_close_matches(prompt, options)
                if closest_matches:
                    suggestion = f"Did you mean `{closest_matches[0]}`?"
                else:
                    suggestion = "Invalid input."
                    
                return Response({'response': suggestion}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
