from rest_framework import serializers, status

from api.v1.games.models import (Game, Question, Answer)


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer class used to work with Game model
    """
    title = serializers.CharField()
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_active = serializers.BooleanField()

    class Meta:
        model = Game
        fields = ('id', 'title', 'created_by', 'is_active')


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer used to work with Question model class
    """
    title = serializers.CharField()
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    points = serializers.IntegerField()
    answers = serializers.SerializerMethodField()

    def get_answers(self, obj):
        try:
            return Answer.objects.filter(question=obj)
        except Answer.DoesNotExist:
            return []

    class Meta:
        model = Question
        fields = ('title', 'points', 'created_by', 'answers')


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer class used to work with Answer model
    """
    answer = serializers.CharField()
    is_correct = serializers.BooleanField()
    question = serializers.SerializerMethodField()
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_question(self, obj):
        try:
            return Question.objects.filter(pk=obj.question_id)
        except Question.DoesNotExist:
            return []

    class Meta:
        model = Answer
        fields = ('question', 'answer', 'is_correct', 'created_by')
