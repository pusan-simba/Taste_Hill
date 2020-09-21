from django.shortcuts import render

# Create your views here.

def start(request):
    return render(request, 'start.html')

def developers(request):
    return render(request, 'developers.html')

def login(request):
    return render(request, 'registration/login.html')

def mymenu(request):
    return render(request, 'mymenu.html')

def mainhome(request):
    return render(request, 'mainhome.html')
