from django.db import models

from api.v1.accounts.models import Account


class GameBaseModel(models.Model):
    """
    Base model used to append default columns for all models
    """
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Game(GameBaseModel):
    title = models.CharField(max_length=255, help_text="The name of the game")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'games'
        ordering = ['-created_at']


class Question(GameBaseModel):
    """
    list of questions used by each game

    """
    title = models.CharField(max_length=255, help_text="Question title/name")
    points = models.IntegerField(help_text="Total points for correct answer", default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'questions'
        ordering = ['-created_at']


class Answer(GameBaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text="Question id.")
    answer = models.CharField(max_length=255, help_text="Answer text assigned to a question")
    is_correct = models.BooleanField(default=False, help_text="Check if the answer is correct.")

    def __str__(self):
        return f'{self.question.title} - {self.answer}'

    class Meta:
        db_table = 'answers'
        ordering = ['-created_at']


class GameQuestions(GameBaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, help_text="Game's identifier")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text="Question's identifier")

    def __str__(self):
        return f'{self.game.title} - {self.question.title}'

    class Meta:
        db_table = 'games_questions'
        ordering = ['-created_at']


class GameResults(models.Model):
    """
    Storing results of the game played by the user.

    """
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="player")
    game = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="game_played")
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.game.title} - {self.user.email}'

    class Meta:
        db_table = 'game_results'
        ordering = ['-played_at']
