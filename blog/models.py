from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE) # If a user is deleted then all of its posts are deleted

    def __str__(self):
        st = f"Title: {self.title}"
        return st

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})