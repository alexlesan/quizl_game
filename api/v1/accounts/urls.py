from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import (LoginAPI, LogoutAPI, RegisterAPI, VerifyEmailAPI)

urlpatterns = [
    path('login/', LoginAPI.as_view(), name="login_api"),
    path('logout/', LogoutAPI.as_view(), name="logout_api"),
    path('register/', RegisterAPI.as_view(), name="register_api"),
    path('email-verify/<str:token>', VerifyEmailAPI.as_view(), name='email_verify'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
