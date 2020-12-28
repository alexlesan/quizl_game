from django.urls import path
from .views import (GameApiView, QuestionApiView, AnswerApiView, GameApiDetail, QuestionApiViewDetail,
                    AnswerApiViewDetail, GameApiSetUpView, GamePlayApiView)

urlpatterns = [
    path('admin/game/', GameApiView.as_view(), name="game_admin_api"),
    path('admin/game/<int:pk>/', GameApiDetail.as_view(), name="game_detail_api"),
    path('admin/game/setup/', GameApiSetUpView.as_view(), name="game_setup"),
    path('admin/question/', QuestionApiView.as_view(), name="game_admin_question"),
    path('admin/question/<int:pk>/', QuestionApiViewDetail.as_view(), name="game_admin_question_detail"),
    path('admin/answer/', AnswerApiView.as_view(), name="game_admin_answer"),
    path('admin/answer/<int:pk>/', AnswerApiViewDetail.as_view(), name="game_admin_answer_detail"),
    path('play/<int:pk>/', GamePlayApiView.as_view(), name="game_play")
]
