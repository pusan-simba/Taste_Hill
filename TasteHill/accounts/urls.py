from django.urls import path
from .views import LoginView,SignupView
urlpatterns = [
    path('login/', LoginView, name="login"),
    path('signup/', SignupView, name="signup")
]