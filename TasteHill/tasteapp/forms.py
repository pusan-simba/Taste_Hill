from django import forms
from accounts.models import MyUser,Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = '__all__'