from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import MajburiyTopshiriq
from .serializer import MajburiyTopshiriqGetSerializer, MajburiyTopshiriqPostSerializer




class UserViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tur']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:  # GET uchun
            return MajburiyTopshiriqGetSerializer
        return MajburiyTopshiriqPostSerializer 