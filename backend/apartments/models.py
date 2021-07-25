from django.db import models

# Create your models here.

class Apartment(models.Model):
    title = models.CharField(max_length=256)
    image = models.URLField(max_length = 200, default="")
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=256, default="")
    description = models.TextField(default="")
    living_area = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    dwelling_type = models.CharField(max_length=256, default="")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title    
    
    class Admin:
        pass