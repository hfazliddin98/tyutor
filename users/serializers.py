from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Users, Fakultet, Yonalish, Kurs, Guruh


class FakultetSerializer(ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name']

class YonalishGetSerializer(ModelSerializer):
    fakultet = FakultetSerializer()
    class Meta:
        model = Yonalish
        fields = ['id', 'fakultet', 'name']

class YonalishPostSerializer(ModelSerializer):
    class Meta:
        model = Yonalish
        fields = ['fakultet', 'name']

class KursGetSerializer(ModelSerializer):
    yonalish = YonalishGetSerializer()
    class Meta:
        model = Kurs
        fields = ['id', 'yonalish', 'name']

class KursPostSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['yonalish', 'name']

class GuruhGetSerializer(ModelSerializer):
    kurs = KursGetSerializer()
    class Meta:
        model = Guruh
        fields = ['id', 'kurs', 'name']

class GuruhPostSerializer(ModelSerializer):
    class Meta:
        model = Guruh
        fields = ['kurs', 'name']



class UserGetSerializer(ModelSerializer):
    guruh= GuruhGetSerializer(many=True, read_only=True)  # ✅ To‘liq ma'lumotni qo‘shish
    fakultet = FakultetSerializer()

    
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'fakultet', 'guruh', 'rasm', 'parol', 'is_active']



class UserPostSerializer(ModelSerializer):
    guruh = PrimaryKeyRelatedField(queryset=Guruh.objects.all(), many=True)  # ✅ Many-to-Many bog‘lanish

    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'fakultet', 'guruh', 'password', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}  # ✅ Parol API javobida chiqmaydi

    def create(self, validated_data):
        guruhlar = validated_data.pop('guruh', [])  
        password = validated_data.pop('password', None)  

        # ✅ Foydalanuvchini yaratish
        user = Users(**validated_data)  
        if password:
            user.set_password(password)  # ✅ Parolni shifrlash
            user.parol = password  # Parolni saqlash (kerak bo'lsa)

        user.save()  

        # ✅ Guruhlarni Many-to-Many bog‘lash
        user.guruh.set(guruhlar)  

        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        guruhlar = validated_data.pop('guruh', None)

        # ✅ Foydalanuvchi ma'lumotlarini yangilash
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password) 
            instance.parol = password  

        instance.save() 

        # ✅ Guruhlarni `.set()` orqali yangilash
        if guruhlar is not None:
            instance.guruh.set(guruhlar)

        return instance
