# from django.db import models

# Create your models here.
from djongo import models

class Test(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.nom