from .models import BoardComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BoardComment
        fields = ('content',)
