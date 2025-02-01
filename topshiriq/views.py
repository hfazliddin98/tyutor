from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from topshiriq.serializers import TopshiriqSerializer, MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer




class TopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.all()
    serializer_class = TopshiriqSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['users']

