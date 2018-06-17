from django.urls import include, path

from rest_framework import routers

from fcm_django.api.rest_framework import FCMDeviceViewSet

from . import views

router = routers.DefaultRouter()
router.register('pins', views.PinViewSet)
router.register('comments', views.CommentViewSet)
router.register('likes', views.LikeViewSet)

urlpatterns = [
    path('devices/', FCMDeviceViewSet.as_view({'post': 'create'}), name='create_fcm_device'),
    path('', include(router.urls)),
]
