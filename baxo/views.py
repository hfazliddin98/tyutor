from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from topshiriq.models import MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq
from baxo.serializers import BaxoMajburiyTopshiriqSerializer, BaxoQoshimchaTopshiriqSerializer, BaxoOzSohasidaTopshiriqSerializer
from baxo.serializers import BaxoOzXohishiBilanTopshiriqSerializer

class BaxoMajburiyTopshiriqViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    serializer_class = BaxoMajburiyTopshiriqSerializer
    http_method_names = ['patch']

class BaxoQoshimchaTopshiriqViewSet(ModelViewSet):
    queryset = QoshimchaTopshiriq.objects.all()
    serializer_class = BaxoQoshimchaTopshiriqSerializer
    http_method_names = ['patch']

class BaxoOzSohasidaTopshiriqViewSet(ModelViewSet):
    queryset = OzSohasidaTopshiriq.objects.all()
    serializer_class = BaxoOzSohasidaTopshiriqSerializer
    http_method_names = ['patch']

class BaxoOzXohishiBilanTopshiriqViewSet(ModelViewSet):
    queryset = OzXohishiBilanTopshiriq.objects.all()
    serializer_class = BaxoOzXohishiBilanTopshiriqSerializer
    http_method_names = ['patch']






