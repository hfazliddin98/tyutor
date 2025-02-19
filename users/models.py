import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from users.choices import UserRoleChoice, KursRoleChoice


class AsosiyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_at']
        abstract = True

class Fakultet(AsosiyModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        full_name = f'{self.name} fakulteti'
        return full_name

class Yonalish(AsosiyModel):
    fakultet = models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        full_name = f'{self.fakultet.name} fakulteti {self.name} yonalishi'
        return full_name

class Kurs(AsosiyModel):
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, choices=KursRoleChoice.choices)

    def __str__(self):
        full_name = f'{self.yonalish.fakultet.name} fakulteti {self.yonalish.name} yonalishi {self.name} kursi'
        return full_name
    
class Guruh(AsosiyModel):
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        full_name = f'{self.kurs.yonalish.fakultet.name} fakulteti {self.kurs.yonalish.name} yonalishi {self.kurs.name} kursi {self.name} guruhi'
        return full_name


class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    role = models.CharField(max_length=30, choices=UserRoleChoice.choices)
    guruh = models.ManyToManyField(Guruh, blank=True)
    rasm = models.ImageField(upload_to='users', blank=True)
    parol = models.CharField(max_length=255, blank=True)


