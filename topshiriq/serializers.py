from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.middleware import get_current_request
from users.choices import UserRoleChoice
from users.serializers import FakultetsSerializer
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq


# Superadmin

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
        read_only_fields = ['topshiriq_turi']
        

class SuperAdminQoshimchaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]
        read_only_fields = ['topshiriq_turi']

class SuperAdminOzSohasidaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]
        read_only_fields = ['topshiriq_turi']


# Admin

class AdminQoshimchaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]
        read_only_fields = ['topshiriq_turi']
        
        
# Topshirqlar
class TopshiriqUserSerializer(ModelSerializer):
    fakultet = FakultetsSerializer()  # Faqatgina GET uchun detallarni ko'rsatadi

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'role', 'fakultet', 'rasm']

class TopshiriqSerializer(ModelSerializer):
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]


class MajburiyTopshiriqSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = MajburiyTopshiriq
        fields = [
            'id', 'user', 'topshiriq', 'tur',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class QoshimchaTopshiriqSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = QoshimchaTopshiriq
        fields = [
            'id', 'user', 'topshiriq',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class OzSohasidaTopshiriqSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = OzSohasidaTopshiriq
        fields = [
            'id', 'user', 'topshiriq',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]

class OzXohishiBilanTopshiriqSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    class Meta:
        model = OzXohishiBilanTopshiriq
        fields = [
            'id', 'user',
            'title', 'body', 'file1', 'file2', 'file3', 'file4'
        ]


