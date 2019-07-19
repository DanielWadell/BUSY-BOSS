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
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]