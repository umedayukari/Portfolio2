from django.urls import path
from . import views
from .views import register_partner

app_name = 'boards'

urlpatterns = [
    path('create_anniversary_record/', views.create_anniversary_record, name='create_anniversary_record'),
    path('anniversary_records/', views.list_anniversary_records, name='list_anniversary_records'),
    path('register_partner/', register_partner, name='register_partner'),
    path('register_present/', views.register_present, name='register_present'),
    path('search/', views.search, name='search'),
]