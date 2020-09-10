from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'registration/start.html')

def developers(request):
    return render(request, 'registration/developers.html')

def register(request):
    return render(request, 'registration/register.html')

def login(request):
    return render(request, 'registration/login.html')

def mymenu(request):
    return render(request, 'restaurant/mymenu.html')

def mainhome(request):
    return render(request, 'restaurant/mainhome.html')
