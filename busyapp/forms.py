from django import forms
from django.core import validators
from busyapp.models import Post,Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        # }
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        # widgets = {
        #     'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        # }
