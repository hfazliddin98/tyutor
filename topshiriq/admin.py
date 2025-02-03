from django.contrib import admin
from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq


@admin.register(SuperAdminTopshiriq)
class TopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(SuperAdminMajburiyTopshiriq)
class MajburiyTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'tur', 'created_at']

@admin.register(SuperAdminQoshimchaTopshiriq)
class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'tur', 'created_at']
