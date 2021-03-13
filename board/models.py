from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    board_image = models.ImageField(upload_to='board/images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'[ {self.pk} ] {self.title} :: {self.author}'

    def get_absolute_url(self):
        return '/board/free_board/{}/'.format(self.pk)


class BoardComment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.content}'

    def get_absolute_url(self):
        return f'{self.board.get_absolute_url()}#comment-{self.pk}'
