from django.shortcuts import render, get_object_or_404, redirect
from busyapp.models import UserInfo,CompanyInfo,Post,Comment
from busyapp.forms import UserForm,CompanyForm,PostForm,CommentForm
from django.utils import timezone
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request,'busyapp/base.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        company_form = CompanyForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_form.save(commit=False)
            profile.user = user

            registered = True
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()
        else:
            print(user_form.errors,user_form.errors)
    else:
        user_form = UserForm()
        company_form = CompanyForm()

    return render(request,'busyapp/registration.html',
                            {'user_form':user_form,
                             'company_form':company_form})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('busyapp:index'))

            else:
                return HttpResponse("You are not active my guy")
        
        else:
            print("Someone is trying to pull a sneaky sneak!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login!!!")
    else:
        return render(request,'busyapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('apptwo:index'))

@login_required
def create_post(request):
    context = {'post':PostForm}
    return render(request,'busyapp/post_form.html',context)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'busyapp/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)