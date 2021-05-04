from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    body = models.TextField()

    def __str__(self):
        return self.title
        return self.comment

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])
        return reverse('home')
