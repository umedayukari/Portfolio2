from django.urls import path
from . import views
from .views import register_opponent

app_name = 'boards'

urlpatterns = [
    path('register_anniversary/', views.register_anniversary, name='register_anniversary'),
    path('anniversary_list/', views.anniversary_records, name='anniversary_list'),
     path('register_opponent/', views.register_opponent, name='register_opponent'),
    path('opponent_list/', views.opponent_list, name='opponent_list'),
    path('search/', views.search, name='search'),
]