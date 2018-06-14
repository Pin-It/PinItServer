from rest_framework import viewsets

from .models import Comment, Like, Pin
from .serializers import CommentSerializer, LikeSerializer, PinSerializer


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all().prefetch_related('comment_set', 'like_set')
    serializer_class = PinSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
