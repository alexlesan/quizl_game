from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import (LoginAPI, LogoutAPI)

urlpatterns = [
    path('login/', LoginAPI.as_view(), name="login_api"),
    path('logout/', LogoutAPI.as_view(), name="logout_api"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
