from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.middleware import get_current_request
from users.choices import UserRoleChoice
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq


class SuperAdminMajburiyTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 
            'majburiy_topshiriq_turi', 'topshiriq_soni', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]

class SuperAdminQoshimchaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]

class AdminQoshimchaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]

        
# Topshirqlar

class MajburiyTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = [
            'id', 'user', 'topshiriq', 'tur',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class QoshimchaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = QoshimchaTopshiriq
        fields = [
            'id', 'user', 'topshiriq',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class OzSohasidaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = OzSohasidaTopshiriq
        fields = [
            'id', 'user',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class OzXohishiBilanTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = OzXohishiBilanTopshiriq
        fields = [
            'id', 'user',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]


