from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from users.models import Users
from users.choices import UserRoleChoice
# from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq


class TopshiriqSerializer(ModelSerializer):
    topshiriq_users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
    class Meta:
        model = Topshiriq
        fields = [
            'id', 'admin_user', 'topshiriq_users', 'topshiriq_turi', 
            'majburiy_topshiriq_turi', 'topshiriq_soni', 'max_baxo',
            'title', 'body', 'file1', 'file2', 'file3', 'file4', 
            'boshlanish_vaqti', 'tugash_vaqti'
        ]

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


# class SuperAdminTopshiriqSerializer(ModelSerializer):
#     users = PrimaryKeyRelatedField(queryset=Users.objects.all(), many=True)  # many=True kerak!
#     class Meta:
#         model = SuperAdminTopshiriq
#         fields = [
#             'id', 'users', 'topshiriq_turi', 'topshiriq_soni', 
#             'title', 'body', 'file1', 'file2', 'file3', 'file4', 
#             'boshlanish_vaqti', 'tugash_vaqti'
#         ]

# class SuperAdminMajburiyTopshiriqSerializer(ModelSerializer):
#     class Meta:
#         model = SuperAdminMajburiyTopshiriq
#         fields = [
#             'id', 'user', 'topshiriq', 'tur',
#             'title', 'body', 'file1', 'file2', 'file3', 'file4'
#         ]

# class SuperAdminQoshimchaTopshiriqSerializer(ModelSerializer):
#     class Meta:
#         model = SuperAdminQoshimchaTopshiriq
#         fields = [
#             'id', 'user', 'topshiriq',
#             'title', 'body', 'file1', 'file2', 'file3', 'file4'
#         ]