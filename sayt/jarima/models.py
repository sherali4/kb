from django.db import models
from django.db.models.functions import Substr

class Hisobotlar(models.Model):
    name = models.CharField(max_length=255)
    izoh = models.TextField()


    def __str__(self):
        return self.name

class Muddati(models.Model):
    hisobot = models.ForeignKey(Hisobotlar, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    izoh = models.TextField()


    def __str__(self):
        return self.hisobot.name + ' (' + self.title + ')'


class Xat_turi(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Baza(models.Model):
    okpo = models.CharField(max_length=8)
    inn = models.CharField(max_length=9)
    nomi = models.CharField(max_length=400)
    soato = models.CharField(max_length=20, blank=True, null=True)
    soato4 = models.CharField(max_length=4, blank=True, null=True)
    soato7 = models.CharField(max_length=7)
    hisobot_nomi = models.ForeignKey(Hisobotlar, on_delete=models.PROTECT)
    topshirish_muddati = models.ForeignKey(Muddati, on_delete=models.CASCADE)
    aniqlangan_sanasi = models.DateField()
    sababi = models.CharField(max_length=400)
    xat_turi = models.ForeignKey(Xat_turi, on_delete=models.CASCADE)
    xat_sanasi = models.DateField()
    chiqib_ketgan = models.BooleanField(default=False)
    izoh = models.TextField()
    notijorat = models.BooleanField(default=False)
    sudga_chiqarilgan = models.BooleanField(default=False)
    tugatilgan = models.BooleanField(default=False)
    dalolatnoma = models.BooleanField(default=False)
    faoliyatsiz = models.BooleanField(default=False)
    huquqbuzarlik_soni = models.IntegerField(default=0)
    yopilgan = models.IntegerField(default=0, blank=True, null=True)



    def __str__(self):
        return self.okpo + ' ' + self.inn + ' ' + self.soato4 + ' ' + self.nomi



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    innx = models.ForeignKey(Baza, on_delete=models.CASCADE)
    # innx = models.IntegerField(default=0, blank=True)
