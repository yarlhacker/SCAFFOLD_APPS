from django.db import models

class Banner(models.Model):

    titre = models.CharField(max_length=255)
    sous_titre = models.TextField()
    image = models.FileField(upload_to = 'banner_image' )

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'

    def __str__(self):
        return self.titre

    

class About(models.Model):
    image = models.FileField()
    titre = models.CharField(max_length=100)
    sous_titre = models.CharField(max_length=300)
    description = models.TextField()
    option = models.ManyToManyField('scaffold_site.Option' , related_name='Options_about',)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.titre


class Option(models.Model):
    liste = models.CharField(max_length=100)

    class Meta():
        verbose_name = 'Option'
        verbose_name_plural = 'Option'

    def __str__(self):
        return self.liste
    

class Team(models.Model):
    image = models.FileField()
    nom = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkdin = models.URLField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.nom


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=100)
    message = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.nom

class Newsletter(models.Model):
    email = models.EmailField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __str__(self):
        return self.email

class Web_site(models.Model):
    nom = models.CharField(max_length=100)
    description_service = models.TextField()
    description_potfolio = models.TextField()
    description_callaction = models.TextField()
    description_testimonial = models.TextField()
    description_team = models.TextField()
    description_pattners = models.TextField()
    description_pack = models.TextField()
    location = models.CharField(max_length=100)
    email = models.EmailField()
    call = models.CharField(max_length=100)
    mapp = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Web_site'
        verbose_name_plural = 'Web_site'

    def __str__(self):
        return self.nom

class Socialcompte(models.Model):
    icon = models.FileField()
    nom = models.CharField(max_length=100)
    lien = models.URLField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Socialcompte'
        verbose_name_plural = 'Socialcompte'

    def __str__(self):
        return self.nom


    

    

# Create your models here.
