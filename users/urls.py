from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FakultetsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'fakultet', FakultetsViewSet, basename='fakultet')


urlpatterns = []
urlpatterns += router.urls