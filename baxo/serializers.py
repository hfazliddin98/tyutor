from rest_framework.serializers import ModelSerializer
from topshiriq.models import MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq


class BaxoMajburiyTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = ['baxo']

class BaxoQoshimchaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = QoshimchaTopshiriq
        fields = ['baxo']

class BaxoOzSohasidaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = OzSohasidaTopshiriq
        fields = ['baxo']

class BaxoOzXohishiBilanTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = OzXohishiBilanTopshiriq
        fields = ['baxo']