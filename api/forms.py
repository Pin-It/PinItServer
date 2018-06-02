from django import forms

from .models import Comment, Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('by_user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('by_user',)
