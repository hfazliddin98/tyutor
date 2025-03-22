from django.db import models

class UserRoleChoice(models.TextChoices):
    SUPERADMIN = ("superadmin", "superadmin")
    ADMIN = ("admin", "admin")
    TYUTOR = ("tutor", "tutor")

class KursRoleChoice(models.TextChoices):
    BIR = ("1", "1")
    IKKI = ("2", "2")
    UCH = ("3", "3")
    TORT = ("4", "4")
    BESH = ("5", "5")



class TalabaChoice(models.TextChoices):
    OGIL= ("o`g`il", "o`g`il")
    QIZ = ("qiz", "qiz")

class TolovChoice(models.TextChoices):
    GRAND= ("grand", "grand")
    KONTRAKT = ("kontrakt", "kontrakt")

        

