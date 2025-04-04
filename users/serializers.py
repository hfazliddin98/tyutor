from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Users, Fakultet, Yonalish, Kurs, Guruh, Talaba


# Talaba

class TalabaGetSerializer(ModelSerializer):
    class Meta:
        model = Talaba
        fields = [
           'id', 'tyutor',
            'familya', 'ism', 'nomer', 'jins', 'sardor', 'tolov_status', 
            'ijtimoiy_ximoya', 'ijtimoiy_daraja', 'iqdidorli_talaba','is_active'
        ]

class TalabaPostSerializer(ModelSerializer):
    class Meta:
        model = Talaba
        fields = [
           'guruh', 'tyutor',
            'familya', 'ism', 'nomer', 'jins', 'sardor', 'tolov_status', 
            'ijtimoiy_ximoya', 'ijtimoiy_daraja', 'iqdidorli_talaba','is_active'
        ]

# Guruh

class GuruhGetSerializer(ModelSerializer):
    talabalar = TalabaGetSerializer(many=True, read_only=True)
    class Meta:
        model = Guruh
        fields = ['id', 'name', 'is_active', 'talabalar']

class GuruhPostSerializer(ModelSerializer):
    class Meta:
        model = Guruh
        fields = ['kurs', 'name', 'is_active']

# Kurs

class KursGetSerializer(ModelSerializer):
    guruhlar = GuruhGetSerializer(many=True, read_only=True)
    class Meta:
        model = Kurs
        fields = ['id', 'name', 'is_active', 'guruhlar']

class KursPostSerializer(ModelSerializer):
    class Meta:
        model = Kurs
        fields = ['yonalish', 'name', 'is_active']

# Yonalish

class YonalishGetSerializer(ModelSerializer):
    kurslar = KursGetSerializer(many=True, read_only=True)
    class Meta:
        model = Yonalish
        fields = ['id', 'name', 'is_active',  'kurslar',]

class YonalishPostSerializer(ModelSerializer):
    class Meta:
        model = Yonalish
        fields = ['fakultet', 'name', 'is_active']

# Fakultet

class FakultetGetSerializer(ModelSerializer):
    yonalishlar = YonalishGetSerializer(many=True, read_only=True)
    class Meta:
        model = Fakultet
        fields = ['id', 'name', 'is_active', 'yonalishlar']

class FakultetPostSerializer(ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['name', 'is_active']



#  user maluotlari uchun


class FakultetSerializer(ModelSerializer):
    class Meta:
        model = Fakultet
        fields = ['id', 'name', 'is_active',]


class YonalishSerializer(ModelSerializer):
    fakultet = FakultetSerializer()
    class Meta:
        model = Yonalish
        fields = ['id', 'name', 'is_active', 'fakultet']

class KursSerializer(ModelSerializer):
    yonalish = YonalishSerializer()
    class Meta:
        model = Kurs
        fields = ['id', 'name', 'is_active', 'yonalish']

class GuruhSerializer(ModelSerializer):
    kurs = KursSerializer()
    class Meta:
        model = Guruh
        fields = ['id', 'name', 'is_active', 'kurs']




class UserGetSerializer(ModelSerializer):
    guruh = GuruhSerializer(many=True, read_only=True)  # ✅ To‘liq ma'lumotni qo‘shish
    fakultet = FakultetGetSerializer()

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
