from django.db import models

# Create your models here.
class student:
    name:str
    address:str
class stud1(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

