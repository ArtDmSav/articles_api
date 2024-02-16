from django.urls import path
from .views import PostList, PostId

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:post_id>', PostId.as_view(), name='post-id'),
]
