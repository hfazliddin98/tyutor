from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
from .serializer import TopshiriqSerializer, MajburiyTopshiriqSerializer, QoshimchaTopshiriqSerializer




class TopshiriqViewSet(ModelViewSet):
    queryset = Topshiriq.objects.all()
    serializer_class = TopshiriqSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['users']

