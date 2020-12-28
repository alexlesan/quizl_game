from rest_framework import serializers

from api.v1.games.models import (Game, Question, Answer, GameQuestions, GameResults)


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer class used to work with Game model
    """
    title = serializers.CharField()
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_active = serializers.BooleanField()

    class Meta:
        model = Game
        fields = ('id', 'title', 'created_by', 'is_active', 'questions')


class GameSetUpSerializer(serializers.ModelSerializer):
    """
    Serializer class used to display game with relation between questions and answers
    """
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GameQuestions
        fields = ('id', 'game', 'question', 'created_by')


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer used to work with Question model class
    """
    title = serializers.CharField()
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    points = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ('id', 'title', 'points', 'created_by', 'answers')


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer class used to work with Answer model
    """
    answer = serializers.CharField()
    is_correct = serializers.BooleanField()
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = ('question', 'answer', 'is_correct', 'created_by')


class GamePlaySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all())
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())
    points = serializers.IntegerField()

    class Meta:
        model = GameResults
        fields = '__all__'

    def create(self, validated_data):
        question = validated_data['question']
        answer = validated_data['answer']
        account = self.context['request'].user
        points_earn = question.points if answer.is_correct else 0

        GameResults.objects.create(
            question=question,
            answer=answer,
            game=validated_data['game'],
            user=account,
            points=points_earn
        )

        if answer.is_correct:
            account.points += points_earn
            account.save()
        return validated_data
