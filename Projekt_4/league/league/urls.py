from django.contrib import admin
from django.urls import path

from . import views
from .views import Table, index, login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', Table.as_view(), name='table'),
    path('', index),
    path('login/', login),
    path('register/', register),
]
