from django.shortcuts import render,redirect, get_object_or_404
from accounts.models import Post,Profile,MyUser,Comment
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm,ReCommentForm

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
    recom_form =  ReCommentForm()
    context['my_post'] = my_post
    context['comment_form'] = comment_form
    context['recom_form'] = recom_form 
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


@login_required
def create_review(request,post_id):
    user = request.user
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        temp_form = filled_form.save(commit=False)
        temp_form.post = Post.objects.get(id =post_id)
        temp_form.user = Profile.objects.get(user=user)
        temp_form.save()
    return redirect('detail',post_id) 



@login_required
def update_review(request,com_id,post_id): # 게시글의 id와 댓글의 id 두개가 필요함.
    my_com = Comment.objects.get(id=com_id)  # 게시글의 id와 댓글의 id 두개가 필요함.
    com_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form =  CommentForm(request.POST, instance = my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail',post_id)
    return render(request,'review_update.html',{'com_form':com_form})
  

    

@login_required
def delete_review(request,com_id,post_id):

    mycom = Comment.objects.get(id=com_id)
    mycom.delete()


    return redirect('detail', post_id)


@login_required
def create_recomment(request,post_id):
    filled_form = ReCommentForm(request.POST)
    if filled_form.is_valid():
        filled_form.save()
    return redirect('detail', post_id)
 