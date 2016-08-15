from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, PostViewSet
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
