from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('images', views.ImageView)

urlpatterns = [
    path('', include(router.urls)),
]