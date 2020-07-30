from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), # name is used in templates {% url 'blog/name' %}
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # primary key is pk
    path('post/new/', PostCreateView.as_view(), name='post-create'), # it will share view with UpdateView => template: post_form
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # this wil automatically use template: post_form
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('announcements/',views.announcements,name='blog-announcements')
]
