from django import forms
from accounts.models import MyUser,Post,Comment,ReComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['body']

class ReCommentForm(forms.ModelForm):

    
    class Meta:
        model = ReComment
        fields = ('body','comment')