from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq
from topshiriq.serializers import SuperAdminTopshiriqSerializer, SuperAdminMajburiyTopshiriqSerializer, SuperAdminQoshimchaTopshiriqSerializer


class SuperAdminTopshiriqViewSet(ModelViewSet):
    queryset = SuperAdminTopshiriq.objects.all()
    serializer_class = SuperAdminTopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topshiriq_turi', 'active']

class SuperAdminMajburiyTopshiriqViewSet(ModelViewSet):
    queryset = SuperAdminMajburiyTopshiriq.objects.all()
    serializer_class = SuperAdminMajburiyTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tur']

class SuperAdminQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = SuperAdminQoshimchaTopshiriq.objects.all()
    serializer_class = SuperAdminQoshimchaTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tur']

