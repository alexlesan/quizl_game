from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CustomAccountManager(BaseUserManager):
    """
    Custom user model manager, the email is the unique identifier for authentication instead of username
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create new user with given data
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        if not email:
            raise ValueError("Please provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save super user with given details
        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.set('is_staff', True)
        extra_fields.set('is_superuser', True)
        extra_fields.set('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Account(AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True)
    points = models.IntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def total_games(self):
        return self.question_set.all().select_related()

    @property
    def rank(self):
        total_games = self.total_games().count()
        return float(self.points / total_games)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        db_table = 'accounts'
        ordering = ['-created_at']
