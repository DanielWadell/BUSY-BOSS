from django.urls import path
from busyapp import views
from django.contrib import admin

app_name = 'busyapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('log_in/',views.user_login,name='login'),
    path('log_out/',views.user_logout,name='logout'),
    path('post_detail/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
]