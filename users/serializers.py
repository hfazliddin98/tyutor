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
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'fakultet', 'rasm', 'parol', 'is_active']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'first_name', 'last_name', 'role', 'fakultet', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}  # Parolni API javobida chiqarilmasligi uchun

    def create(self, validated_data):
        # Foydalanuvchini yaratish
        password = validated_data.pop('password', None)
        user = Users(**validated_data)

        if password:
            user.set_password(password)  # Parolni shifrlash
            user.parol = password
        user.save()

        return user

    def update(self, instance, validated_data):
        # Foydalanuvchini yangilash
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Parolni shifrlash
            instance.parol = password

        instance.save()

        return instance

