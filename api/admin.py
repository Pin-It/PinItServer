from django.contrib import admin

from .models import Comment, Pin, UserProfile

admin.site.register(Pin)
admin.site.register(Comment)
admin.site.register(UserProfile)
