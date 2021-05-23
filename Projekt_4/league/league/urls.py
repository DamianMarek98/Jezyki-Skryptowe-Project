from django.contrib import admin
from django.urls import path, include
from .views import Table, index, login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', Table.as_view(), name='table'),
    path('', index),
    path('', include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
]
