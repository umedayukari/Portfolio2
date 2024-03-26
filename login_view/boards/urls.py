from django.urls import path
from . import views
from .views import register_opponent, list_anniversary_records, delete_anniversary_record

app_name = 'boards'

urlpatterns = [
    path('register_anniversary/', views.register_anniversary, name='register_anniversary'),
    path('anniversary_list/', views.list_anniversary_records, name='anniversary_list'),
    path('anniversary/edit/<int:id>/', views.edit_anniversary_record, name='edit_anniversary_record'),
    path('anniversary/delete/<int:id>/', delete_anniversary_record, name='delete_anniversary_record'),
    path('anniversary/list/', list_anniversary_records, name='anniversary_records'),
    path('register_opponent/', views.register_opponent, name='register_opponent'),
    path('opponent_list/', views.opponent_list, name='opponent_list'),
    path('opponent/edit/<int:id>/', views.edit_opponent, name='edit_opponent'),
    path('opponent/delete/<int:id>/', views.delete_opponent, name='delete_opponent'),
]    