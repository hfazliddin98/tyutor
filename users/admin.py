from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import Users, Fakultets

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display  = [
        'username', 'first_name', 'last_name',
        'parol', 'is_superuser', 'is_active'
    ]
    list_filter = [
        'superadmin', 
        'admin',
        'tyutr'
    ]

@admin.register(Fakultets)
class FakultetsAdmin(admin.ModelAdmin):
    list_display  = [
        'name', 
    ]
    

admin.site.unregister(Group)