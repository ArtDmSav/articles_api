from django.urls import path

from .views import PostList, PostId, AuthorList, AuthorId, CommentList, CommentId, UserList, UserId

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostId.as_view(), name='post-id'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorId.as_view(), name='author-id'),
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentId.as_view(), name='comment-id'),
    path('users/', UserList.as_view(), name='author-list'),
    path('users/<int:pk>/', UserId.as_view(), name='author-id'),
]
