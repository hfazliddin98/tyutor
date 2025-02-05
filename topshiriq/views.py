from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from users.choices import UserRoleChoice
from topshiriq.choices import TopshiriqTuriChoice
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from topshiriq.models import OzSohasidaTopshiriq, OzXohishiBilanTopshiriq
from topshiriq.serializers import MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer
from topshiriq.serializers import OzSohasidaTopshiriqSerializer, OzXohishiBilanTopshiriqSerializer
from topshiriq.serializers import SuperAdminMajburiyTopshiriqSerializer, SuperAdminQoshimchaTopshiriqSerializer,AdminQoshimchaTopshiriqSerializer
from topshiriq.serializers import SuperAdminTestTopshiriqSerializer



class SuperAdminMajburiyTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.MAJBURIY)
    serializer_class = SuperAdminMajburiyTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']

class SuperAdminQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)
    serializer_class = SuperAdminQoshimchaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']

class SuperAdminTestTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.TEST)
    serializer_class = SuperAdminTestTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']

class AdminQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.ADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)
    serializer_class = AdminQoshimchaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active']


class MajburiyTopshiriqViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    serializer_class = MajburiyTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'baxolash', 'tur']

class QoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = QoshimchaTopshiriq.objects.all()
    serializer_class = QoshimchaTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'baxolash']

class OzSohasidaTopshiriqViewSet(ModelViewSet):
    queryset = OzSohasidaTopshiriq.objects.all()
    serializer_class = OzSohasidaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'baxolash']

class OzXohishiBilanTopshiriqViewSet(ModelViewSet):
    queryset = OzXohishiBilanTopshiriq.objects.all()
    serializer_class = OzXohishiBilanTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['active', 'baxolash']



