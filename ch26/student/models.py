from django.db import models

# Create your models here.


class profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        # return f"{self.name} - {self.email} - {self.city}"
        return str(self.id)


class result(models.Model):
    st_class = models.CharField(max_length=50)
    st_roll = models.CharField(max_length=50)
    st_marks = models.IntegerField(max_length=50)

    def __str__(self):
        # return f"{self.name} - {self.email} - {self.city}"
        return str(self.st_roll)