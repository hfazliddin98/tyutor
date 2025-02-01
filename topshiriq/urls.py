from django.urls import path
from rest_framework.routers import DefaultRouter
from topshiriq.views import TopshiriqViewSet

router = DefaultRouter()
router.register(r'topshiriq', TopshiriqViewSet)


urlpatterns = []
urlpatterns += router.urls
