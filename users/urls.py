from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, FakultetsViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'fakultets', FakultetsViewSet)


urlpatterns = []
urlpatterns += router.urls