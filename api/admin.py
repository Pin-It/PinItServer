from django.contrib import admin

from .forms import PinForm
from .models import Comment, Pin, UserProfile

admin.site.register(Comment)
admin.site.register(UserProfile)


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    form = PinForm
