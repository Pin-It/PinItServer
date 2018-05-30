from rest_framework import serializers

from .models import Comment, Pin


class PinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pin
        fields = ('pin_type', 'latitude', 'longitude')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('pin', 'text')
