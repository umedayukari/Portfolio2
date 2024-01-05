
from django.contrib import admin
from django.urls import path, include

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),  # accountsアプリのurlsをインクルード
    path('home/', include('accounts.urls')),  # homeのURLをaccountsアプリのurlsに含める場合
]