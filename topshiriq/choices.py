from django.db import models
        

class TopshiriqTuriChoice(models.TextChoices):
    MAJBURIY = ("majburiy", "majburiy")
    QOSHIMCHA = ("qoshimcha", "qoshimcha")
    OZ_SOHASIDA = ("oz_sohasida", "oz_sohasida")



class MajburiyTopshiriqTuriChoice(models.TextChoices):
    TTJGA_TASHRIF = ("ttjga_tashrif", "ttjga_tashrif")
    IJARAGA_TASHRIF = ("ijaraga_tashrif", "ijaraga_tashrif")
    TUTORLIK_SOATI = ("tutorlik_soati", "tutorlik_soati")
    DAVRA_SUHBATI = ("davra_suhbati", "davra_suhbati")
    TADBIR = ("tadbir", "tadbir")
    TOGARAK = ("togarak", "togarak")
    TTJDA_TADBIR = ("ttjda_tadbir", "ttjda_tadbir")
    IQDIDORLI_TALABAM = ("iqtidorli_talabam", "iqtidorli_talabam")
    OILAGA_XAT = ("oilaga_xat", "oilaga_xat")
    TEST = ("test", "test")

class TalabaChoice(models.TextChoices):
    OGIL= ("o`g`il", "o`g`il")
    QIZ = ("qiz", "qiz")

class TolovChoice(models.TextChoices):
    GRAND= ("grand", "grand")
    KONTRAKT = ("kontrakt", "kontrakt")

class TestChoice(models.TextChoices):
    A= ("A", "A")
    B= ("B", "B")
    C= ("C", "C")
    D = ("D", "D")



