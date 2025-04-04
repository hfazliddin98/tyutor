from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import Signal, receiver
from topshiriq.models import MajburiyTopshiriq




@receiver(pre_save, sender=MajburiyTopshiriq)
def majburiy_update(sender, instance, **kwargs):
    if instance.pk:  # Agar ID bor bo‘lsa, demak obyekt yangilanmoqda
        print(f"Custom signal (update) ishga tushdi: {instance}")
    else:  # Agar ID yo‘q bo‘lsa, demak yangi obyekt
        print(f"Custom signal (create) ishga tushdi: {instance}")