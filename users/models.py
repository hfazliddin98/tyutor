import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class AsosiyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    class Meta:
        abstract = True

class Fakultets(AsosiyModel):
    name = models.CharField(max_length=255)





class Users(AbstractUser):
    class RoleChoice(models.TextChoices):
        SUPERADMIN = ("superadmin", "superadmin")
        ADMIN = ("admin", "admin")
        TUTOR = ("tutor", "tutor")
        

    role = models.CharField(max_length=30, choices=RoleChoice.choices)
    fakultet = models.ForeignKey(Fakultets, on_delete=models.CASCADE, null=True)
    rasm = models.ImageField(upload_to='users', blank=True)
    parol = models.CharField(max_length=255, blank=True)


