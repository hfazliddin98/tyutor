from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq, Testlar
# from topshiriq.models import SuperAdminTopshiriq, SuperAdminMajburiyTopshiriq, SuperAdminQoshimchaTopshiriq


@admin.register(Topshiriq)
class TopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['title', 'active', 'vaqt_tugadi']

@admin.register(MajburiyTopshiriq)
class MajburiyTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'baxolash', 'created_at']

@admin.register(QoshimchaTopshiriq)
class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
    list_display  = ['id', 'user', 'baxolash', 'created_at']



@admin.register(Testlar)
class TestlarAdmin(ImportExportModelAdmin):
    list_display  = ['id']

# @admin.register(SuperAdminQoshimchaTopshiriq)
# class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
#     list_display  = ['id', 'user', 'created_at']
