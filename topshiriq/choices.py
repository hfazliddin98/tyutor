from django.db import models
        

class TopshiriqTuriChoice(models.TextChoices):
    MAJBURIY = ("majburiy", "majburiy")
    QOSHIMCHA = ("qoshimcha", "qoshimcha")



class MajburiyTopshiriqTuriChoice(models.TextChoices):
    TTJGA_TASHRIF = ("ttjga_tashrif", "ttjga_tashrif")
    IJARAGA_TASHRIF = ("ijaraga_tashrif", "ijaraga_tashrif")
    TUTORLIK_SOATI = ("tutorlik_soati", "tutorlik_soati")
    DAVRA_SUHBATI = ("davra_suhbati", "davra_suhbati")
    TADBIR = ("tadbir", "tadbir")
    TTJDA_TADBIR = ("ttjda_tadbir", "ttjda_tadbir")
    IQDIDORLI_TALABAM = ("iqtidorli_talabam", "iqtidorli_talabam")
    OILAGA_XAT = ("oilaga_xat", "oilaga_xat")
    TEST = ("test", "test")

