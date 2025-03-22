from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import Users, Fakultet, Yonalish, Kurs, Guruh, Talaba

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display  = [
        'username', 'first_name', 'last_name', 'role',
        'is_superuser', 'is_active'
    ]


@admin.register(Fakultet)
class FakultetAdmin(admin.ModelAdmin):
    list_display  = [
        'name', 
    ]

@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    list_display  = [
        'name', 
    ]

@admin.register(Kurs)
class KursAdmin(admin.ModelAdmin):
    list_display  = [
        'name', 
    ]

@admin.register(Guruh)
class GuruhAdmin(admin.ModelAdmin):
    list_display  = [
        'name', 
    ]

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display  = ['id']
    

admin.site.unregister(Group)