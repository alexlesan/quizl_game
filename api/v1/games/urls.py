from django.urls import path
from .views import (GameApiView, QuestionApiView, AnswerApiView)

urlpatterns = [
    path('admin/game/', GameApiView.as_view(), name="game_admin_api"),
    path('admin/question/', QuestionApiView.as_view(), name="game_admin_question"),
    path('admin/answer/', AnswerApiView.as_view(), name="game_admin_answer"),
]
