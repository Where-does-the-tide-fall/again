from django.shortcuts import render, redirect
from django.http import JsonResponse
from start_again.models import User


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username, password=password)
        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        try:
            user = User.objects.create(username=username, password=password)
        except User.DoesNotExist:
            return JsonResponse({'message': 'login failed'})
        else:
            response = JsonResponse({'message': 'login success'})
            if remember == 'true':
                response.set_cookie('username', username, max_age=7 * 24 * 3600)
            return response
