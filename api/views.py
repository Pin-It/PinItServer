from rest_framework import viewsets

from .models import Comment, Pin
from .serializers import CommentSerializer, PinSerializer


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
