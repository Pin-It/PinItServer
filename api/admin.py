from django.contrib import admin

from .forms import CommentForm, PinForm
from .models import Comment, Pin, UserProfile

admin.site.register(UserProfile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    form = PinForm
