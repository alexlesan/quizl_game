from pprint import pprint

import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.urls import reverse
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.v1.accounts.models import Account
from api.v1.accounts.permission import IsGuest
from api.v1.accounts.serializers import LoginSerializer, LogoutSerializer, RegisterSerializer, \
    EmailVerificationSerializer
from api.v1.accounts.utils import SendUserEmail


class LoginAPI(GenericAPIView):
    """
    View used to login in the user based on received data
    """
    serializer_class = LoginSerializer
    permission_classes = (IsGuest,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"data": serializer.data, "msg": "Login successfully"}, status=status.HTTP_200_OK)


class LogoutAPI(GenericAPIView):
    """
    Logout user view
    """
    serializer_class = LogoutSerializer
    permissions = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": [], "msg": "Logout successfully."}, status=status.HTTP_200_OK)


class RegisterAPI(APIView):
    """
    Register new user functionality.
    """
    serializer_class = RegisterSerializer
    permission_classes = [IsGuest]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            account = Account.objects.get(email__iexact=serializer.data['email'])
            current_site = get_current_site(request)
            token = RefreshToken.for_user(account).access_token
            activate_url = reverse('email_verify', args=[token])
            email_data = {
                "user": account,
                "domain_url": current_site,
                "activate_url": activate_url
            }
            SendUserEmail.send_registration_email(email_data)
            return Response({"data": serializer.data, "token":account.tokens()}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailAPI(APIView):
    """
    Verify registered account by email url
    """
    serializer_class = EmailVerificationSerializer

    def get(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Account.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_active = True
                user.save()
            return Response({
                "data": [],
                'msg': 'Successfully activated'
            }, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'data': [], 'msg': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'data': [], 'msg': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
