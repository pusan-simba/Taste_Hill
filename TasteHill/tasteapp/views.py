from django.shortcuts import render,redirect, get_object_or_404
from accounts.models import Post, Profile,MyUser
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm

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
    context = dict()
    post_form = Post.objects.all()
    context['post_form']= post_form
    return render(request, 'mainhome.html',context)


def detail(request,post_id):
    context = dict()
    my_post = get_object_or_404(Post,pk=post_id)
    comment_form = CommentForm()
    context['my_post'] = my_post
    context['comment_form'] = comment_form

    return render(request,'detail.html',context)


@login_required
def post_like_toggle(request,post_id):
    post = get_object_or_404(Post, pk=post_id) 
    user = request.user                        
    profile = Profile.objects.get(user=user) 
    try:
        check_like = profile.like_post.get(id=post_id)
        profile.like_post.remove(post) 
        post.like_count -= 1 
        post.save()
    except:
        profile.like_post.add(post)
        post.like_count += 1 
        
        post.save() 

    return redirect('detail', post_id) 

