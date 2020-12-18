from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class LoginAPI(GenericAPIView):
    def post(self, request, *args, **kwargs):
        pass

class LogoutAPI(GenericAPIView):
     def post(self, request):
         pass
