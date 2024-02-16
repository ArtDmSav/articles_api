from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
