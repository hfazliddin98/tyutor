from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from topshiriq.serializers import TopshiriqSerializer, MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer
from topshiriq.serializers import SuperAdminTopshiriqSerializer,AdminTopshiriqSerializer


class TopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.all()
    serializer_class = TopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['topshiriq_turi', 'active']


class MajburiyTopshiriqViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    serializer_class = MajburiyTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tur']

class QoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = QoshimchaTopshiriq.objects.all()
    serializer_class = QoshimchaTopshiriqSerializer
    http_method_names = ['get', 'patch']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']



