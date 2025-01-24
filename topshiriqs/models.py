from django.db import models
from users.choices import MajburiyTopshiriqTurChoice
from users.models import AsosiyModel, Users


class MajburiyTopshiriq(AsosiyModel):
    tur = models.CharField(max_length=30, choices=MajburiyTopshiriqTurChoice.choices)
    users = models.ManyToManyField(Users, related_name='majburiytopshiriq', blank=True)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    file1 = models.FileField(upload_to='topshiriq')
    file2 = models.FileField(upload_to='topshiriq')
    qiymat = models.CharField(max_length=20, blank=True)
    baxo = models.CharField(max_length=20, blank=True)
    boshlanishi = models.DateField()
    tugash = models.DateField()
    



