from django.urls import path
from blog.api.views import *

# api/blog/
urlpatterns = [
    # path('posts/', api_post_list_view, name='api-post-list'),
    path('posts/', ApiPostListView.as_view(), name='api-post-list'),
    path('post/<int:pk>/update/', api_post_update_view, name='api-post-update'),
    path('post/<int:pk>/delete/', api_post_delete_view, name='api-post-delete'),
    path('post/<int:pk>/', api_post_detail_view, name='api-post-detail'),
    path('post/new/', api_post_create_view, name='api-post-create'),
]