from django.urls import path
from .views import UserDetailsView

urlpatterns = [
    path('user/', UserDetailsView.as_view(), name='user_details'),
]
