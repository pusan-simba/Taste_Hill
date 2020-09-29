from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget= forms.PasswordInput(
    attrs = {'class': 'form-contorl','type':'password', 'name':'password1'}),
    label="Password")
    password2 = forms.CharField(widget= forms.PasswordInput(
        attrs= {'class':'form-control','type':'password', 'name':'password2'}),
    label="Password 확인")
    
    class Meta:
        model = MyUser
        fields = ('email','nickname','password1','password2')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())