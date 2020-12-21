from django.shortcuts import render
from rest_framework import mixins
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView

from api.v1.games.models import Game, Question, Answer
from api.v1.games.serializers import GameSerializer, QuestionSerializer, AnswerSerializer


class GameApiView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericAPIView):
    """
    Class used to create, update, delete a game
    Permission is allowed only for Admin users
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class QuestionApiView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericAPIView):
    """
    Class used to create/update/delete Question
    Permission allowed only for Admin users
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AnswerApiView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    Class used to create/update/delete an answer
    Permissions allowed only for Admin users
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
