from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from api.v1.accounts.models import Account


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer used to validate and check inputs for login user process
    """
    email = serializers.EmailField(min_length=6, max_length=80, required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'tokens', 'password')

    def validate(self, data):
        email = data.get('email', '')
        password = data.get('password', '')
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again.')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin.')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens(),
        }


class LogoutSerializer(serializers.Serializer):
    """
    Serializer used to logout user
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, data):
        self.token = data['refresh']
        return data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class RegisterSerializer(serializers.ModelSerializer):
    """
    Registration Serializer, validate and treat user's inputs from registration page
    """
    email = serializers.EmailField(min_length=6, max_length=60, required=True,
                                   validators=[UniqueValidator(queryset=Account.objects.all())])
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=Account.objects.all())])
    password = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Account.objects.create_user(
            email=validated_data['email'], password=validated_data['password'],
            username=validated_data['username']
        )
        return user


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Account
        fields = ['token']
