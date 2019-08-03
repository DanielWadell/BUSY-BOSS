from django.urls import path
from busyapp import views
from django.contrib import admin

app_name = 'busyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register_user/',views.register_user,name='register_user'),
    path('log_in/',views.user_login,name='login'),
    path('log_out/',views.user_logout,name='logout'),
    path('post/publish/<int:pk>/', views.post_publish, name='post_publish'),
    path('post/details/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/',views.CreatePostView.as_view(),name='create_post'),
    path('drafts/', views.PostListView.as_view(), name='post_draft_list'),
    path('post/edit/<int:pk>', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/remove/<int:pk>/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]