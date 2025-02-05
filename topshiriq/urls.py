from django.urls import path
from rest_framework.routers import DefaultRouter
from topshiriq.views import MajburiyTopshiriqViewSet, QoshimchaTopshiriqViewSet
from topshiriq.views import OzSohasidaTopshiriqViewSet, OzXohishiBilanTopshiriqViewSet
from topshiriq.views import AdminQoshimchaTopshiriqViewSet, SuperAdminMajburiyTopshiriqViewSet, SuperAdminQoshimchaTopshiriqViewSet

router = DefaultRouter()
router.register(r'superadmin_majburiy_topshiriq', SuperAdminMajburiyTopshiriqViewSet, basename='superadmin_majburiy_topshiriq')
router.register(r'superadmin_qoshimcha_topshiriq', SuperAdminQoshimchaTopshiriqViewSet, basename='superadmin_qoshimcha_topshiriq')
router.register(r'admin_qoshimcha_topshiriq', AdminQoshimchaTopshiriqViewSet, basename='admin_qoshimcha_topshiriq')
router.register(r'majburiy', MajburiyTopshiriqViewSet, basename='majburiy')
router.register(r'qoshimcha', QoshimchaTopshiriqViewSet, basename='qoshimcha')
router.register(r'oz_sohasida', OzSohasidaTopshiriqViewSet, basename='ozsohasida')
router.register(r'oz_xohishi_bilan', OzXohishiBilanTopshiriqViewSet, basename='oz_xohishi_bilan')


urlpatterns = []
urlpatterns += router.urls
