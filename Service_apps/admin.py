from django.contrib import admin
from . import models

admin.site.register(models.Prestation)
admin.site.register(models.Service)
admin.site.register(models.Faq)
admin.site.register(models.Pack)
admin.site.register(models.Avantage)

# Register your models here.
