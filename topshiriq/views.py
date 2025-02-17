from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from users.choices import UserRoleChoice
from topshiriq.choices import TopshiriqTuriChoice
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from topshiriq.models import OzSohasidaTopshiriq, OzXohishiBilanTopshiriq
from topshiriq.serializers import MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer
from topshiriq.serializers import OzSohasidaTopshiriqSerializer, OzXohishiBilanTopshiriqSerializer
from topshiriq.serializers import SuperAdminMajburiyTopshiriqSerializer, SuperAdminQoshimchaTopshiriqSerializer, SuperAdminOzSohasidaTopshiriqSerializer
from topshiriq.serializers import SuperAdminMajburiyTopshiriqSerializer, SuperAdminQoshimchaTopshiriqSerializer,AdminQoshimchaTopshiriqSerializer



# Superadmin

class SuperAdminMajburiyTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.MAJBURIY)
    serializer_class = SuperAdminMajburiyTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def perform_create(self, serializer):
        serializer.save(topshiriq_turi=TopshiriqTuriChoice.MAJBURIY)


class SuperAdminQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)
    serializer_class = SuperAdminQoshimchaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def perform_create(self, serializer):
        serializer.save(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)

class SuperAdminOzSohasidaTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.SUPERADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.OZ_SOHASIDA)
    serializer_class = SuperAdminOzSohasidaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def perform_create(self, serializer):
        serializer.save(topshiriq_turi=TopshiriqTuriChoice.OZ_SOHASIDA)


# Admin

class AdminQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.filter(admin_user__role=UserRoleChoice.ADMIN).filter(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)
    serializer_class = AdminQoshimchaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []

    def perform_create(self, serializer):
        serializer.save(topshiriq_turi=TopshiriqTuriChoice.QOSHIMCHA)


# Topshiriqlar

class MajburiyTopshiriqViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    serializer_class = MajburiyTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topshiriq__active', 'baxolash', 'tur']


class QoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = QoshimchaTopshiriq.objects.all()
    serializer_class = QoshimchaTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['baxolash']


class OzSohasidaTopshiriqViewSet(ModelViewSet):
    queryset = OzSohasidaTopshiriq.objects.all()
    serializer_class = OzSohasidaTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['baxolash']


class OzXohishiBilanTopshiriqViewSet(ModelViewSet):
    queryset = OzXohishiBilanTopshiriq.objects.all()
    serializer_class = OzXohishiBilanTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['baxolash']



