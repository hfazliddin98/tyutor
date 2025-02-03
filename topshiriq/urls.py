from django.urls import path
from rest_framework.routers import DefaultRouter
from topshiriq.views import TopshiriqViewSet, MajburiyTopshiriqViewSet, QoshimchaTopshiriqViewSet
# from topshiriq.views import SuperAdminTopshiriqViewSet, SuperAdminMajburiyTopshiriqViewSet, SuperAdminQoshimchaTopshiriqViewSet

router = DefaultRouter()
router.register(r'topshiriq', TopshiriqViewSet)
router.register(r'majburiy', MajburiyTopshiriqViewSet)
router.register(r'qoshimcha', QoshimchaTopshiriqViewSet)
# router.register(r'topshiriq', SuperAdminTopshiriqViewSet)
# router.register(r'majburiy', SuperAdminMajburiyTopshiriqViewSet)
# router.register(r'qoshimcha', SuperAdminQoshimchaTopshiriqViewSet)


urlpatterns = []
urlpatterns += router.urls
