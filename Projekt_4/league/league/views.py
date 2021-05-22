from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Team


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        return render(request, 'league/login.html')
    else:
        return index(request)


def register(request):
    if request.user.is_authenticated:
        return render(request, 'league/register.html')
    else:
        return index(request)


class Table(ListView):
    model = Team
