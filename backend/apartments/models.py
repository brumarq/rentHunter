from django.db import models

# Create your models here.

class Apartment(models.Model):
    title = models.CharField(max_length=256)
    price = models.BigIntegerField()

    class Meta:
        ordering = ['title']