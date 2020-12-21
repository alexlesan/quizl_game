from rest_framework import mixins
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView

from api.v1.games.models import Game, Question, Answer
from api.v1.games.serializers import GameSerializer, QuestionSerializer, AnswerSerializer


class GameApiView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
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


class GameApiDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    """
    Class used to get/update and delete game by id
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @permission_classes((permissions.IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionApiView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
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


class QuestionApiViewDetail(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):
    """
    Class used to get/update and delete question by id
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @permission_classes((permissions.IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AnswerApiView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):
    """
    Class used to create/update/delete an answer
    Permissions allowed only for Admin users
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get(self, request, *args, **kwargs):
        """
        get the list of answers with pagination
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create new Answer, insert new row in database
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return self.create(request, *args, **kwargs)


class AnswerApiViewDetail(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          GenericAPIView):
    """
    Class used to get/update and delete answer by id
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @permission_classes((permissions.IsAuthenticated,))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes((permissions.IsAdminUser,))
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
