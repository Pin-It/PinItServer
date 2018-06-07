from django.contrib import admin

from .models import Comment, Pin, UserProfile

admin.site.register(UserProfile)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'pin', 'text', 'by_user')
    list_display_links = list_display
    readonly_fields = ('created_at',)


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ('id', 'pin_type', 'latitude', 'longitude', 'by_user')
    list_display_links = list_display
    readonly_fields = ('created_at',)
