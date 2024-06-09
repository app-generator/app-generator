from apps.api.chat.v1.serializers import ChatSerializer
from apps.api.product.v1.serializers import ProductSerializer
from apps.common.models import Products, Type
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from difflib import get_close_matches
import base64
from datetime import datetime


def html_to_base64(html_content):
    html_bytes = html_content.encode('utf-8')
    base64_bytes = base64.b64encode(html_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


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
                html_content = self.generate_html(product_serializer.data)
                base64_html = html_to_base64(html_content)
                return Response({'response': "Products rendered successfully!", 'content': base64_html, 'type': 'products'}, status=status.HTTP_200_OK)
            elif 'app' in prompt:
                products = Products.objects.filter(type=Type.WEBAPP)
                product_serializer = ProductSerializer(products, many=True)
                html_content = self.generate_html(product_serializer.data)
                base64_html = html_to_base64(html_content)
                return Response({'response': "Products rendered successfully!", 'content': base64_html, 'type': 'products'}, status=status.HTTP_200_OK)
            elif 'api' in prompt:
                products = Products.objects.filter(type=Type.API)
                product_serializer = ProductSerializer(products, many=True)
                html_content = self.generate_html(product_serializer.data)
                base64_html = html_to_base64(html_content)
                return Response({'response': "Products rendered successfully!", 'content': base64_html, 'type': 'products'}, status=status.HTTP_200_OK)
            else:
                closest_matches = get_close_matches(prompt, options)
                if closest_matches:
                    suggestion = f"Did you mean `{closest_matches[0]}`?"
                else:
                    suggestion = "Invalid input."
                    
                return Response({'response': suggestion}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def generate_html(self, products):
        html_content = ""
        for product in products:
            release_date = datetime.strptime(product['release_date'], '%Y-%m-%d')
            formatted_date = release_date.strftime('%d %B %Y')
            html_content += f"""
                <div class="rounded-3xl p-4 md:p-6 border-2">
                    <div class="relative rounded-2xl aspect-[4/3] overflow-hidden">
                        <a target="_blank" href="/product/{product['design']}/{product['tech1']}/">
                            <img src="media/product/{product['design']}/{product['tech1']}/top.png" alt="{product['name']}" width="100%" height="auto" class="w-full aspect-[4/3] object-cover hover:scale-105 transition-transform duration-150 ease-in-out" />
                        </a>
                    </div>
                    <div class="pt-3.5">
                        <div class="text-sm flex items-center justify-between text-blue-500">
                            <span>{formatted_date}</span>
                            <span class="font-medium text-gray-800 line-clamp-2 text-sm overflow-hidden">
                                {'FREE' if product['free'] else '$' + str(product['price'])}
                            </span>
                        </div>
                        <h2 class="font-semibold text-gray-800 line-clamp-2 text-ellipsis overflow-hidden my-3">
                            <a target="_blank" href="/product/{product['design']}/{product['tech1']}/" class="text-gray-800">{product['name']}</a>
                        </h2>
                        <p class="text-sm line-clamp-2 text-ellipsis overflow-hidden mb-3">{product['info']}</p>
                        <div class="flex items-center justify-between">
                            <a target="_blank" href="/product/{product['design']}/{product['tech1']}/" class="text-sm hover:underline">Read more</a>
                        </div>
                    </div>
                </div>
            """
        return html_content
