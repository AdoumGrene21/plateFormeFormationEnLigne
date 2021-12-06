from django.db import models

# Create your models here.
class Forma(models.Model):
    libelle = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle