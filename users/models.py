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

    def __str__(self):
        return self.name



class Users(AbstractUser):
    superadmin = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    tyutr = models.BooleanField(default=False)
    fakultet = models.ForeignKey(Fakultets, on_delete=models.CASCADE)
    rasm = models.ImageField(upload_to='users', null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
