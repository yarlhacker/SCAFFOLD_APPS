from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100,null=False , blank=False)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'

    def __str__(self):
        return self.nom

class Carde(models.Model):
    
    titre = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField()
    titre.detail = models.CharField(max_length=100)
    detail =  models.TextField()
    client = models.CharField(max_length=100)
    date_projet = models.DateField()
    url = models.URLField(max_length=100)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Carde'
        verbose_name_plural = 'Carde'
    
    def __str__(self):
        return self.titre

class Testimonial(models.Model):
    image = models.FileField()
    nom = models.CharField(max_length=100)
    description = models.TextField()
    metier = models.CharField(max_length=100)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonial'

    def __str__(self):
        return self.nom

class Pattners(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.FileField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Pattners'
        verbose_name_plural = 'Pattners'

    def __str__(self):
        return self.nom
        

class Image(models.Model):
    image = models.FileField()
    cadre = models.ForeignKey(Carde , null= True, related_name='carde_images',on_delete=models.SET_NULL, blank=False )


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Image'
        verbose_name_plural = 'Image'

# Create your models here.
