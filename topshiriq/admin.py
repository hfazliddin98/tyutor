from django.contrib import admin
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq, Test, TestTopshiriq, TestJavob, TestNatija
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

@admin.register(Test)
class TestlarAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(TestTopshiriq)
class TestTopshiriqlarAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(TestJavob)
class TestJavoblarAdmin(admin.ModelAdmin):
    list_display  = ['id']

@admin.register(TestNatija)
class TestNatijalarAdmin(admin.ModelAdmin):
    list_display  = ['id']

# @admin.register(SuperAdminQoshimchaTopshiriq)
# class QoshimchaTopshiriqAdmin(admin.ModelAdmin):
#     list_display  = ['id', 'user', 'created_at']
