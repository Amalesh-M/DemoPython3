from django.db import models
# Create your models here.
from django.db.models import TextField


class Place(models.Model):
    name=models.CharField(max_length=350)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    name = models.CharField(max_length=350)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
