
from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    # path(_("teach-me/")+"<topic>/", views.teach_me_topic, name='teach_me_topic'),
    path("ai-processor/", views.teach_me, name="teach_me"),
    path("ai-processor/<str:tag>/", views.teach_me, name="teach_me_with_tag"),
    path("ai-processor/r/list/", views.question_list, name="response_list"),
    path("ai-processor/r/list/<str:tag>", views.question_list, name="response_list_with_tag"),
    path("ask/", views.ask_question, name="ask_question"),
    path('thread/<int:thread_id>/messages/', views.thread_messages, name='thread_messages'),
]
