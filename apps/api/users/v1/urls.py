from django.urls import path
from .views import UserDetailsView, StatusViewAPI

urlpatterns = [
    path('user/', UserDetailsView.as_view(), name='user_details'),

    path('django-generator-status/', StatusViewAPI.as_view(), name='user_details'),
]
