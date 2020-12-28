from django.contrib.auth.decorators import permission_required
from rest_framework import mixins, status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.accounts.permission import IsSuperUser
from api.v1.games.models import Game, Question, Answer, GameQuestions
from api.v1.games.serializers import GameSerializer, QuestionSerializer, AnswerSerializer, GameSetUpSerializer, \
    GamePlaySerializer


class GameApiView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  GenericAPIView):
    """
    Class used to create, update, delete a game
    Permission is allowed only for Admin users
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (IsSuperUser,)

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

    @permission_classes([IsSuperUser])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes([IsSuperUser])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GameApiSetUpView(mixins.ListModelMixin, mixins.CreateModelMixin,
                       GenericAPIView):
    """
    Class used to create the game, assign question and answers
    """
    permission_classes = (IsSuperUser,)
    serializer_class = GameSetUpSerializer
    queryset = GameQuestions.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuestionApiView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      GenericAPIView):
    """
    Class used to create/update/delete Question
    Permission allowed only for Admin users
    """
    permission_classes = (IsSuperUser,)
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

    @permission_classes([IsSuperUser])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_classes([IsSuperUser])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AnswerApiView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):
    """
    Class used to create/update/delete an answer
    Permissions allowed only for Admin users
    """
    permission_classes = (IsSuperUser,)
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

    @permission_required('is_superuser')
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @permission_required('is_superuser')
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GamePlayApiView(mixins.RetrieveModelMixin, GenericAPIView):
    """
    class used to play the game by the user
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    """
    get the game details
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    """ 
    method used to store results for a game
     """
    def post(self, request, *args, **kwargs):
        serializer = GamePlaySerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "msg": "successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"data": serializer.errors, "msg": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
