from django.db import models

class UserRoleChoice(models.TextChoices):
    SUPERADMIN = ("superadmin", "superadmin")
    ADMIN = ("admin", "admin")
    TUTOR = ("tutor", "tutor")
        

class MajburiyTopshiriqTurChoice(models.TextChoices):
    TTJGA_TASHRIF = ("ttjga_tashrif", "ttjga_tashrif")
    IJARAGA_TASHRIF = ("ijaraga_tashrif", "ijaraga_tashrif")
    TUTORLIK_SOATI = ("tutorlik_soati", "tutorlik_soati")
    DAVRA_SUHBATI = ("davra_suhbati", "davra_suhbati")
    TADBIR = ("tadbir", "tadbir")
    TTJDA_TADBIR = ("ttjda_tadbir", "ttjda_tadbir")
    IQDIDORLI_TALABAM = ("iqtidorli_talabam", "iqtidorli_talabam")
    OILAGA_XAT = ("oilaga_xat", "oilaga_xat")
