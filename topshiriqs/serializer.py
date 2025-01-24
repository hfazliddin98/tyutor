from rest_framework.serializers import ModelSerializer
from .models import MajburiyTopshiriq


class MajburiyTopshiriqGetSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = ['id', 'tur']

class MajburiyTopshiriqPostSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = ['id', 'tur']