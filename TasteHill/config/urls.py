"""TasteHill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from tasteapp.views import start, developers, mymenu, mainhome,detail,post_like_toggle,create_review,delete_review,update_review,create_recomment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start, name="start"),
    path('tasteapp/developers/', developers, name="developers"),
    path('tasteapp/mymenu/', mymenu, name="mymenu"),
    path('tasteapp/mainhome/', mainhome, name="mainhome"),
    path('accounts/',include('accounts.urls')),
    path('tasteapp/detail/<int:post_id>',detail,name="detail"),
    path('tasteapp/post_like_toggle/<int:post_id>',post_like_toggle, name="post_like_toggle"),
    path('tasteapp/create_review/<int:post_id>',create_review,name="create_review"), 
    path('tasteapp/delete_review/<int:post_id>/<int:com_id>',delete_review , name="delete_review"),
    path('tasteapp/update_review/<int:post_id>/<int:com_id>',update_review , name="update_review"),
    path('tasteapp/create_recomment/<int:post_id>',create_recomment , name="create_recomment"),

]
