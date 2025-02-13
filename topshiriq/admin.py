from django.contrib import admin
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq
# from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq


@admin.register(Topshiriq)
class TopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['title']

@admin.register(MajburiyTopshiriq)
class MajburiyTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['user', 'created_at']

@admin.register(QoshimchaTopshiriq)
class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['user', 'created_at']

# @admin.register(SuperAdminTopshiriq)
# class TopshiriqAdmin(admin.ModelAdmin):
#     list_display  = ['id']

# @admin.register(SuperAdminMajburiyTopshiriq)
# class MajburiyTopshiriqAdmin(admin.ModelAdmin):
#     list_display  = ['id', 'user', 'created_at']

# @admin.register(SuperAdminQoshimchaTopshiriq)
# class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
#     list_display  = ['id', 'user', 'created_at']
