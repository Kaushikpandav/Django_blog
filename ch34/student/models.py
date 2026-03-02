from django.db import models

# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=300 , blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name