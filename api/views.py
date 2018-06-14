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

    def get_queryset(self):
        '''
        Only return the likes created by the current user.
        Optional `pin` parameter is used to filter the list by associated pin
        '''
        user = self.request.user
        queryset = Like.objects.filter(by_user_id=user.id)
        pin = self.request.query_params.get('pin', None)
        if pin is not None:
            queryset = queryset.filter(pin=pin)
        return queryset
