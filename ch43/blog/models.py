from django.db import models

# Create your models here.
class underconstruction(models.Model):
  is_under_construction = models.BooleanField(default=False)
  note  = models.TextField(blank=True, null=True, help_text='Note for admin')
  duration = models.DurationField(blank=True, null=True, help_text='Duration for admin')
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.note