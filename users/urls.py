from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FakultetsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'fakultet', FakultetsViewSet)


urlpatterns = []
urlpatterns += router.urls