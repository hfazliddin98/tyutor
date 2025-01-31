from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.choices import UserRoleChoice
from .models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq


class TopshiriqSerializer(ModelSerializer):
    users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
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