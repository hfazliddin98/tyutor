from django.db import models
from topshiriq.choices import TopshiriqTuriChoice, MajburiyTopshiriqTuriChoice, TestChoice
from users.models import AsosiyModel, Users




class Topshiriq(AsosiyModel):
    admin_user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, blank=True) # superadmin yoki admin uchun
    topshiriq_users = models.ManyToManyField(Users, related_name="users")  # kopgina userlar uchun
    topshiriq_turi = models.CharField(max_length=30, choices=TopshiriqTuriChoice.choices, default=TopshiriqTuriChoice.QOSHIMCHA)
    majburiy_topshiriq_turi = models.CharField(max_length=30, choices=MajburiyTopshiriqTuriChoice.choices, null=True, blank=True)
    topshiriq_soni = models.IntegerField(default=1)
    max_baxo = models.IntegerField(default=0)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/topshiriq', null=True, blank=True)
    active = models.BooleanField(default=False)
    vaqt_tugadi = models.BooleanField(default=False)
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
    baxo = models.IntegerField(default=0)
    file1 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/majburiy', null=True, blank=True)
    baxolash = models.BooleanField(default=False)

        
    def __str__(self):
        return self.title

    
class QoshimchaTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    baxo = models.IntegerField(default=0)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    admin = models.BooleanField(default=False)
    baxolash = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    
class OzSohasidaTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE)
    baxo = models.IntegerField(default=0)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    baxolash = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
class OzXohishiBilanTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    baxo = models.IntegerField(default=0)
    title = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    file1 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file2 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file3 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    file4 = models.FileField(upload_to='topshiriq/qoshimcha', null=True, blank=True)
    baxolash = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Test(AsosiyModel):
    matn = models.TextField(verbose_name="Savol matni")
    variant_a = models.CharField(max_length=255)
    variant_b = models.CharField(max_length=255)
    variant_c = models.CharField(max_length=255)
    variant_d = models.CharField(max_length=255)
    togri_javob = models.CharField(
        max_length=1,
        choices=TestChoice.choices,
        verbose_name="To‘g‘ri javob",
        default=TestChoice.A
    )

    def __str__(self):
        return self.matn
    
class TestTopshiriq(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE) # tyutor uchun
    topshiriq = models.ForeignKey(Topshiriq, on_delete=models.CASCADE, related_name='topshiriqlar')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)


class TestJavob(AsosiyModel):
    test_topshiriq = models.ForeignKey(TestTopshiriq, on_delete=models.CASCADE, related_name='javoblar')
    tanlangan_javob = models.CharField(max_length=1)  # A/B/C/D
    togri = models.BooleanField(default=False)


class TestNatija(AsosiyModel):
    topshiriq = models.OneToOneField(Topshiriq, on_delete=models.CASCADE, related_name='natijalar')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    togri_soni = models.IntegerField()
    jami_soni = models.IntegerField()
    foiz = models.FloatField()




    
 