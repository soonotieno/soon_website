from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=30)
    content = models.TextField()

    created = models.DateTimeField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
