from django.db import models

# Create your models here.


class Students(models.Model):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Students"
        
    def __str__(self):
        return self.name
    