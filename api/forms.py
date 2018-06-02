from django import forms

from .models import Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        exclude = ('by_user',)
