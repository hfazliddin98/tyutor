from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from topshiriq.serializers import TopshiriqSerializer, MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer
# from topshiriq.serializers import SuperAdminTopshiriqSerializer, SuperAdminMajburiyTopshiriqSerializer, SuperAdminQoshimchaTopshiriqSerializer
# from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq


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

# class SuperAdminTopshiriqViewSet(ModelViewSet):
#     queryset = SuperAdminTopshiriq.objects.all()
#     serializer_class = SuperAdminTopshiriqSerializer
#     http_method_names = ['get', 'post', 'patch', 'delete']
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['topshiriq_turi', 'active']

# class SuperAdminMajburiyTopshiriqViewSet(ModelViewSet):
#     queryset = SuperAdminMajburiyTopshiriq.objects.all()
#     serializer_class = SuperAdminMajburiyTopshiriqSerializer
#     http_method_names = ['get', 'patch']
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['tur']

# class SuperAdminQoshimchaTopshiriqViewSet(ModelViewSet):
#     queryset = SuperAdminQoshimchaTopshiriq.objects.all()
#     serializer_class = SuperAdminQoshimchaTopshiriqSerializer
#     http_method_names = ['get', 'patch']
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['tur']

