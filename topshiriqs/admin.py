from django.contrib import admin
from topshiriqs.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq


@admin.register(Topshiriq)
class TopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(MajburiyTopshiriq)
class MajburiyTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(QoshimchaTopshiriq)
class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id']
