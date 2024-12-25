from rest_framework import serializers
from .models import Users, Fakultets


class FakultetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultets
        fields = ['id', 'name']



class UserGetSerializer(serializers.ModelSerializer):
    fakultet = FakultetsSerializer()  # Faqatgina GET uchun detallarni ko'rsatadi

    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'role', 'fakultet', 'rasm', 'is_active']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'first_name', 'last_name', 'role', 'fakultet', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}  # Parolni API javobida chiqarilmasligi uchun



