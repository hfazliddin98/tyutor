from django.db import models
from topshiriq.choices import TopshiriqTuriChoice, MajburiyTopshiriqTuriChoice, QoshimchaTopshiriqTuriChoice
from users.models import AsosiyModel, Users


class Topshiriq(AsosiyModel):
    users = models.ManyToManyField(Users, related_name="users")  # kopgina userlar uchun
    topshiriq_turi = models.CharField(max_length=30, choices=TopshiriqTuriChoice.choices)
    urinishlar_soni = models.CharField(max_length=2, blank=True)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    boshlanish_vaqti = models.DateField()
    tugash_vaqti = models.DateField()

    def __str__(self):
        return self.title

class MajburiyTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    tur = models.CharField(max_length=30, choices=MajburiyTopshiriqTuriChoice.choices)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
        
    def __str__(self):
        return self.title
    
class QoshimchaTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    tur = models.CharField(max_length=30, choices=QoshimchaTopshiriqTuriChoice.choices)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)

    def __str__(self):
        return self.title

