from django.contrib import admin
from django.urls import path, include
from accounts.views import RegistUserView, CustomLoginView, UserLogoutView, HomeView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', RegistUserView.as_view(), name='register'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),
]
