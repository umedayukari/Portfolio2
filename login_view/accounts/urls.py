from django.contrib import admin
from django.urls import path, include
from accounts.views import RegistUserView, CustomLoginView, UserLogoutView
from .views import HomeView


app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('register/', RegistUserView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
]
