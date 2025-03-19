from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.middleware import get_current_request
from users.choices import UserRoleChoice
from users.serializers import FakultetSerializer, GuruhSerializer
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq, OzSohasidaTopshiriq, OzXohishiBilanTopshiriq, Talabalar


# Superadmin

class SuperAdminMajburiyTopshiriqPostSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'topshiriq_users',
            'majburiy_topshiriq_turi', 'topshiriq_soni', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
        ]
        read_only_fields = ['topshiriq_turi']
        

class SuperAdminMajburiyTopshiriqGetSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users',
            'majburiy_topshiriq_turi', 'topshiriq_soni', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
        ]
        
        

class SuperAdminQoshimchaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
        ]
        read_only_fields = ['topshiriq_turi']

class SuperAdminOzSohasidaTopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'topshiriq_users', 'topshiriq_turi', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
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
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
        ]
        read_only_fields = ['topshiriq_turi']
        
        
# Topshirqlar
class TopshiriqUserSerializer(ModelSerializer):
    fakultet = FakultetSerializer()  # Faqatgina GET uchun detallarni ko'rsatadi

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'role', 'fakultet', 'rasm', 'is_active']

class TopshiriqSerializer(ModelSerializer):
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti', 'is_active'
        ]


class MajburiyTopshiriqGetSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = MajburiyTopshiriq
        fields = [
            'id', 'user', 'topshiriq', 'tur',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class MajburiyTopshiriqPostSerializer(ModelSerializer):
    class Meta:
        model = MajburiyTopshiriq
        fields = [
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class QoshimchaTopshiriqGetSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = QoshimchaTopshiriq
        fields = [
            'id', 'user', 'topshiriq',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class QoshimchaTopshiriqPostSerializer(ModelSerializer):
    class Meta:
        model = QoshimchaTopshiriq
        fields = [
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class OzSohasidaTopshiriqGetSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    topshiriq = TopshiriqSerializer()
    class Meta:
        model = OzSohasidaTopshiriq
        fields = [
            'id', 'user', 'topshiriq',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class OzSohasidaTopshiriqPostSerializer(ModelSerializer):

    class Meta:
        model = OzSohasidaTopshiriq
        fields = [
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class OzXohishiBilanTopshiriqGetSerializer(ModelSerializer):
    user = TopshiriqUserSerializer()
    class Meta:
        model = OzXohishiBilanTopshiriq
        fields = [
            'id', 'user',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class OzXohishiBilanTopshiriqPostSerializer(ModelSerializer):
    class Meta:
        model = OzXohishiBilanTopshiriq
        fields = [
           'user', 'title', 'body', 'file1', 'file2', 'file3', 'file4', 'is_active'
        ]

class TalabalarGetSerializer(ModelSerializer):
    tyutor = TopshiriqUserSerializer()
    guruh= GuruhSerializer(many=True, read_only=True)  # ✅ To‘liq ma'lumotni qo‘shish
    class Meta:
        model = Talabalar
        fields = [
           'id','guruh', 'tyutor',
            'familya', 'ism', 'jins', 'sardor', 'tolov_status', 
            'ijtimoiy_ximoya', 'ijtimoiy_daraja', 'iqdidorli_talaba','is_active'
        ]

class TalabalarPostSerializer(ModelSerializer):
    class Meta:
        model = Talabalar
        fields = [
           'guruh', 'tyutor',
            'familya', 'ism', 'jins', 'sardor', 'tolov_status', 
            'ijtimoiy_ximoya', 'ijtimoiy_daraja', 'iqdidorli_talaba','is_active'
        ]


