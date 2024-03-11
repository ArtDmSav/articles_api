from django.urls import path

from .views import PostList, PostId, AuthorList, AuthorId, CommentList, CommentId

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostId.as_view(), name='post-id'),
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorId.as_view(), name='author-id'),
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentId.as_view(), name='comment-id'),
]
