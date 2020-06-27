from django.db import models

class NormalProd(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=55)
    price = models.FloatField()
    description = models.TextField(max_length=24000)
    slug = models.SlugField()
class PromoProd(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=55)
    price = models.FloatField()
    description = models.TextField(max_length=24000)
class about(models.Model):
    about = models.TextField(max_length=25000)
class service(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(max_length=25000)