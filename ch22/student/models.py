from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)
    roll =  models.IntegerField(max_length=10)
    state = models.CharField(max_length=50)
    comment = models.TextField(max_length=500, default = "No comment")

    # IntegerField
    # BigIntegerField
    # AutoField
    # FloatField
    # CharField
    # TextField
    # BooleanField
    # EmailField
    # URLField
    # BinaryField
