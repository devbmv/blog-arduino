from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.


def index(request):
    return HttpResponse("<h1>Arduino Blog</h1>")


def debug_view(request):
    return HttpResponse(f"DEBUG = {settings.DEBUG}")
