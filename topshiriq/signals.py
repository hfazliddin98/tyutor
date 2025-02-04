from django.db.models.signals import post_save, m2m_changed
from users.middleware import get_current_request
from django.dispatch import receiver
from users.choices import UserRoleChoice
from topshiriq.choices import TopshiriqTuriChoice
from topshiriq.models import Topshiriq, MajburiyTopshiriq, QoshimchaTopshiriq 




# Flag saqlash uchun dictionary
processing_tasks = {}

@receiver(post_save, sender=Topshiriq)
def create_topshiriq(sender, instance, created, **kwargs):
    """Topshiriq yaratildi yoki yangilandi"""
    request = get_current_request()
    if created:
        if request and request.user:  # Request mavjudligini tekshiramiz
            instance.admin_user = request.user  # Admin userni saqlaymiz
            instance.save(update_fields=["admin_user"])  # O‘zgarishni saqlaymiz
            print(f"Topshiriq yaratildi: {instance.id}, Admin: {request.user.username}")
        
        # Flag qo‘yamiz, shunda m2m_changed signalidan foydalanish mumkin bo‘ladi
        processing_tasks[instance.pk] = True

@receiver(m2m_changed, sender=Topshiriq.topshiriq_users.through)
def task_users_added(sender, instance, action, **kwargs):
    """Foydalanuvchilar qo‘shilganda ishlaydi"""
    request = get_current_request()

    if action == "post_add" and processing_tasks.get(instance.pk):

        if request.user.role == UserRoleChoice.SUPERADMIN:
            if instance.topshiriq_turi == TopshiriqTuriChoice.MAJBURIY:
                for user in instance.topshiriq_users.all():
                    for _ in range(int(instance.topshiriq_soni)):
                        MajburiyTopshiriq.objects.create(
                            user=user,  # To‘g‘ri foydalanuvchini saqlash
                            topshiriq=instance,  # ID emas, obyektning o‘zi
                            tur=instance.majburiy_topshiriq_turi
                        )

            if instance.topshiriq_turi == TopshiriqTuriChoice.QOSHIMCHA:
                for user in instance.topshiriq_users.all():
                    for _ in range(int(instance.topshiriq_soni)):
                        QoshimchaTopshiriq.objects.create(
                            user=user,  # To‘g‘ri foydalanuvchini saqlash
                            topshiriq=instance
                        )

        if request.user.role == UserRoleChoice.ADMIN:
            if instance.topshiriq_turi == TopshiriqTuriChoice.QOSHIMCHA:
                for user in instance.topshiriq_users.all():
                    for _ in range(int(instance.topshiriq_soni)):
                        QoshimchaTopshiriq.objects.create(
                            user=user, 
                            topshiriq=instance # ID emas, obyektning o‘zi
                        )

        # Signal ishlaganidan keyin flagni olib tashlaymiz
        processing_tasks.pop(instance.pk, None)
