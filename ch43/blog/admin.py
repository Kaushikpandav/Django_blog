from django.contrib import admin
from .models import underconstruction

# Register your models here.


@admin.register(underconstruction)
class underconstructionAdmin(admin.ModelAdmin):
  list_display = ['is_under_construction', 'note', 'duration', 'updated_at', 'created_at']
