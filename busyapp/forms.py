from django import forms
from django.core import validators
from busyapp.models import CompanyInfo,Post
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class CompanyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = CompanyInfo
        fields = ('company_username',)

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title','text',)