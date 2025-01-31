from rest_framework.serializers import ModelSerializer
from .models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq


class TopshiriqSerializer(ModelSerializer):
    class Meta:
        model = Topshiriq
        fields = ['id', 'users', 'topshiriq_turi', 'urinishlar_soni', 'boshlanish_vaqti', 'tugash_vaqti']

class MajburiyTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = ['id', 'tur']

class QoshimchaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = QoshimchaTopshiriq
        fields = ['id', 'tur']