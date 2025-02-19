from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FakultetViewSet, YonalishViewSet, KursViewSet, Guruh

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'fakultet', FakultetViewSet, basename='fakultet')
router.register(r'yonalish', YonalishViewSet, basename='yonalish')
router.register(r'kurs', KursViewSet, basename='kurs')
router.register(r'guruh', Guruh, basename='guruh')


urlpatterns = []
urlpatterns += router.urls