from django.db import models

# Create your models here.
class Patient(models.Model):
    breed = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)