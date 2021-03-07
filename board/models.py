from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # author:추후작성

    def __str__(self):
        return f'[ {self.pk} ] {self.title} {self.created_at}'
