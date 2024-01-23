from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create_theme/', views.create_theme, name='create_theme'),
    path('list_themes/', views.list_themes, name='list_themes'),
    path('register_partner/', views.register_partner, name='register_partner'),
    path('register_present/', views.register_present, name='register_present'),
    path('search/', views.search, name='search'),
]