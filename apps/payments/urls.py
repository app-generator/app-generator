from django.urls import path
from apps.payments import views


urlpatterns = [
    path('api/create-checkout-session/', views.create_checkout_session, name="create_checkout_session"),
    path('success/', views.success, name="success"),
    path('cancel/', views.cancel, name="cancel"),
]
