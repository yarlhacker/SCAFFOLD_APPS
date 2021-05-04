from django.db import models


class Service (models.Model):
    icon = models.FileField()
    image = models.FileField()
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=225)
    color = models.CharField(max_length=225)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Service'

    def __str__(self):
        return self.titre


class Prestation(models.Model):
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Prestation'
        verbose_name_plural = 'Prestation'

    def __str__(self):
        return self.titre
    

class Faq(models.Model):
    question = models.CharField(max_length=100)
    response = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta():
        verbose_name = 'Faq'
        verbose_name_plural = 'Faq'

    def __str__(self):
        return self.question


class Avantage(models.Model):
    libele = models.CharField(max_length=100)
    barre = models.BooleanField(default=False)
    pack =models.ForeignKey('Service_apps.Pack', on_delete=models.SET_NULL, null=True , related_name='packs_avantage')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Avantage'
        verbose_name_plural = 'Avantage'

class Pack(models.Model):
    titre = models.CharField(max_length=100,null=False , blank=False)
    prix = models.FloatField()
    periode = models.DateField()
    etiquet = models.BooleanField()
    color = models.BooleanField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Pack'
        verbose_name_plural = 'Pack'

    def __str__(self):
        return self.titre

# Create your models here.
