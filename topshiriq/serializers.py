from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.choices import UserRoleChoice
from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq


class SuperAdminTopshiriqSerializer(ModelSerializer):
    users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = SuperAdminTopshiriq
        fields = [
            'id', 'users', 'topshiriq_turi', 'topshiriq_soni', 
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]

class SuperAdminMajburiyTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = SuperAdminMajburiyTopshiriq
        fields = [
            'id', 'user', 'topshiriq', 'tur',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class SuperAdminQoshimchaTopshiriqSerializer(ModelSerializer):
    class Meta:
        model = SuperAdminQoshimchaTopshiriq
        fields = [
            'id', 'user', 'topshiriq', 'tur',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]