from django.urls import path
from apps.support import views


urlpatterns = [
    path('create/', views.create_support_ticket, name="create_support_ticket"),
    path('all-tickets/', views.all_tickets, name="all_tickets"),
    path('my-tickets/', views.my_tickets, name="my_tickets"),
    path('comment/<int:ticket_id>/', views.comment_to_ticket, name="comment_to_ticket"),
]
