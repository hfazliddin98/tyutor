from django.db import models
from topshiriqs.choices import TopshiriqTuriChoice, MajburiyTopshiriqTuriChoice, QoshimchaTopshiriqTuriChoice
from users.models import AsosiyModel, Users


class Topshiriq(AsosiyModel):
    users = models.ManyToManyField(Users, related_name="users")
    topshiriq_turi = models.CharField(max_length=30, choices=TopshiriqTuriChoice.choices)
    urinishlar_soni = models.CharField(max_length=2, blank=True)
    boshlanish_vaqti = models.DateField()
    tugash_vaqti = models.DateField()


class MajburiyTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    tur = models.CharField(max_length=30, choices=MajburiyTopshiriqTuriChoice.choices)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    file1 = models.FileField(upload_to='topshiriq/majburiy')
    file2 = models.FileField(upload_to='topshiriq/majburiy')
    file3 = models.FileField(upload_to='topshiriq/majburiy')
    file4 = models.FileField(upload_to='topshiriq/majburiy')

class QoshimchaTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    tur = models.CharField(max_length=30, choices=QoshimchaTopshiriqTuriChoice.choices)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    file1 = models.FileField(upload_to='topshiriq/qoshimcha')
    file2 = models.FileField(upload_to='topshiriq/qoshimcha')
    file3 = models.FileField(upload_to='topshiriq/qoshimcha')
    file4 = models.FileField(upload_to='topshiriq/qoshimcha')

    



