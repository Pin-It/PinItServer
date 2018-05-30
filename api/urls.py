from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pins', views.PinViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
