from django.urls import path
from apps.ticket import views


urlpatterns = [
    path('create/', views.create_support_ticket, name="create_support_ticket"),
    path('operate-ticket/', views.oeprate_ticket, name="oeprate_ticket"),
    path('comment/<int:ticket_id>/', views.comment_to_ticket, name="comment_to_ticket"),
]
