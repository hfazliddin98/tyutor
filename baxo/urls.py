from rest_framework.routers import DefaultRouter
from baxo.views import BaxoMajburiyTopshiriqViewSet, BaxoQoshimchaTopshiriqViewSet, BaxoOzSohasidaTopshiriqViewSet
from baxo.views import BaxoOzXohishiBilanTopshiriqViewSet



router = DefaultRouter()

router.register(r'baxo_majburiy_topshiriq', BaxoMajburiyTopshiriqViewSet, basename='baxo_majburiy_topshiriq')
router.register(r'baxo_qoshimcha_topshiriq', BaxoQoshimchaTopshiriqViewSet, basename='baxo_qoshimcha_topshiriq')
router.register(r'baxo_oz_sohasida_topshiriq', BaxoOzSohasidaTopshiriqViewSet, basename='baxo_oz_sohasida_topshiriq')
router.register(r'baxo_oz_xohishi_bilan_topshiriq', BaxoOzXohishiBilanTopshiriqViewSet, basename='baxo_oz_xohishi_bilan_topshiriq')


urlpatterns = []
urlpatterns += router.urls