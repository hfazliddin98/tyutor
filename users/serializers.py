from rest_framework import serializers
from .models import Users, Fakultet, Yonalish, Kurs, Guruh


class FakultetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']

class YonalishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yonalish
        fields = ['id', 'fakultet', 'name']

class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['id', 'yonalish', 'name']

class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = ['id', 'kurs', 'name']



class UserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'guruh', 'rasm', 'parol', 'is_active']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'first_name', 'last_name', 'role', 'guruh', 'password', 'is_active']
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

