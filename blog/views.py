from rest_framework import generics
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostId(APIView):
    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']  # Получаем значение из URL.
        try:
            queryset = Post.objects.get(id=post_id)  # Получаем пост с нужным id
            serializer_class = PostSerializer(queryset)  # Сериализуем полученный пост
            return JsonResponse(serializer_class.data)  # Возвращаем данные в формате JSON
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post does not exist'}, status=status.HTTP_404_NOT_FOUND)
