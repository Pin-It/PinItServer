from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pins', views.PinViewSet)
router.register('comments', views.CommentViewSet)
router.register('likes', views.LikeViewSet)
router.register('device-location', views.DeviceLocationViewSet)

urlpatterns = [
    path('devices/', views.DeviceViewSet.as_view({'post': 'create'}),
         name='create_fcm_device'),
    path('device-location/<device__registration_id>/', views.DeviceLocationViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('', include(router.urls)),
]
