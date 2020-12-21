from django.urls import path
from .views import (GameApiView, QuestionApiView, AnswerApiView, GameApiDetail, QuestionApiViewDetail,
                    AnswerApiViewDetail)

urlpatterns = [
    path('admin/game/', GameApiView.as_view(), name="game_admin_api"),
    path('admin/game/<int:pk>/', GameApiDetail.as_view(), name="game_detail_api"),
    path('admin/question/', QuestionApiView.as_view(), name="game_admin_question"),
    path('admin/question/<int:pk>/', QuestionApiViewDetail.as_view(), name="game_admin_question_detail"),
    path('admin/answer/', AnswerApiView.as_view(), name="game_admin_answer"),
    path('admin/answer/<int:pk>/', AnswerApiViewDetail.as_view(), name="game_admin_answer_detail"),
]
