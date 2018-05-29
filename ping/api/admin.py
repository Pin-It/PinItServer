from django.contrib import admin

from .models import Comment, Pin

admin.site.register(Pin)
admin.site.register(Comment)
