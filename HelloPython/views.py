from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello_views(request):
    return HttpResponse('<h1>Hello Python</h1>')
