from django.db import models


# Create your models here.
class Member(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return self.email