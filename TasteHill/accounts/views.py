from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm
from .models import MyUser,UserManager
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
            else:
                return redirect('login')
    form=LoginForm
    return render(request,'login.html',{'form':form})

def SignupView(request):
    if request.method == "POST":
        form = SignupForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('signup')
    
    form = SignupForm
    return render(request, 'signup.html',{'form':form})
        