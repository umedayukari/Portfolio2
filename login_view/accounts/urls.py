from django.urls import path
from .views import CustomLoginView, UserLogoutView, RegistUserView, HomeView


app_name = 'accounts'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),  
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('home/', HomeView.as_view(), name='home'),
]


