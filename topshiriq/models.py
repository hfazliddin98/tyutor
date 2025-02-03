from django.db import models
from topshiriq.choices import TopshiriqTuriChoice, MajburiyTopshiriqTuriChoice
from users.models import AsosiyModel, Users


class  SuperAdminTopshiriq(AsosiyModel):
    users = models.ManyToManyField(Users, related_name="users")  # kopgina userlar uchun
    topshiriq_turi = models.CharField(max_length=30, choices=TopshiriqTuriChoice.choices)
    topshiriq_soni = models.CharField(max_length=2, blank=True)
    max_baxo = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    active = models.BooleanField(default=True)
    boshlanish_vaqti = models.DateField()
    tugash_vaqti = models.DateField()

    def __str__(self):
        return self.title

class SuperAdminMajburiyTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(SuperAdminTopshiriq, on_delete=models.CASCADE)
    tur = models.CharField(max_length=30, choices=MajburiyTopshiriqTuriChoice.choices)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    baxo = models.CharField(max_length=3, blank=True)
    file1 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)

        
    def __str__(self):
        return self.title
    
class SuperAdminQoshimchaTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(SuperAdminTopshiriq, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    baxo = models.CharField(max_length=3, blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)

    def __str__(self):
        return self.title


# Zam dekan kiritadigan topshiriq

class  AdminTopshiriq(AsosiyModel):
    users = models.ManyToManyField(Users, related_name="users")  # kopgina userlar uchun
    max_baxo = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    active = models.BooleanField(default=True)
    boshlanish_vaqti = models.DateField()
    tugash_vaqti = models.DateField()

    def __str__(self):
        return self.title

    
class AdminQoshimchaTopshiriq(AsosiyModel):
    admin_user = models.ForeignKey(Users, on_delete=models.CASCADE) # admin uchun
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(AdminTopshiriq, on_delete=models.CASCADE)
    baxo = models.CharField(max_length=3, blank=True)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)

    def __str__(self):
        return self.title

