from django.contrib import admin
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq


@admin.register(Topshiriq)
class TopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(MajburiyTopshiriq)
class MajburiyTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'tur', 'created_at']

@admin.register(QoshimchaTopshiriq)
class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'tur', 'created_at']
