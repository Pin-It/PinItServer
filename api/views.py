from fcm_django.models import FCMDevice
from fcm_django.api.rest_framework import FCMDeviceViewSet

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from .models import Comment, Like, Pin, DeviceLocation
from .serializers import CommentSerializer, LikeSerializer, PinSerializer, \
    DeviceLocationSerializer


class PinViewSet(viewsets.ModelViewSet):
    queryset = Pin.objects.all().prefetch_related('comment_set', 'like_set')
    serializer_class = PinSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet, mixins.DestroyModelMixin):
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


class DeviceLocationViewSet(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = DeviceLocation.objects.all()
    serializer_class = DeviceLocationSerializer
    lookup_field = 'device__registration_id'
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        return DeviceLocation.objects.filter(device__user_id=user.id)

    def get_object(self):
        user = self.request.user
        device_token = self.kwargs[self.lookup_field]
        device = get_object_or_404(FCMDevice.objects.all(),
                                   registration_id=device_token,
                                   user_id=user.id,
                                   active=True)
        (obj, _) = self.get_queryset().get_or_create(device=device)
        self.check_object_permissions(self.request, obj)
        return obj


class DeviceViewSet(FCMDeviceViewSet):
    permission_classes = (AllowAny,)
