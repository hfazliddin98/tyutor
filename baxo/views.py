from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from topshiriq.models import MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq
from baxo.serializers import BaxoMajburiyTopshiriqSerializer, BaxoQoshimchaTopshiriqSerializer, BaxoOzSohasidaTopshiriqSerializer
from baxo.serializers import BaxoOzXohishiBilanTopshiriqSerializer

class BaxoMajburiyTopshiriqViewSet(ModelViewSet):
    queryset = MajburiyTopshiriq.objects.all()
    serializer_class = BaxoMajburiyTopshiriqSerializer
    http_method_names = ['patch']

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.baxo > 0:
            print(f'{instance.baxo}')
            instance.baxolash = True  # updated_at maydonini hozirgi vaqtga o‘zgartiramiz
            instance.save()  # O‘zgarishlarni saqlaymiz
        else:
            print(f'singanl ishlamadi')

        return Response({"message": "Obyekt yangilandi!"}, status=status.HTTP_200_OK)

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






