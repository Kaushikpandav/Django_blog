from django.contrib import admin
from .models import profile, result

admin.site.register(profile)
# class profileAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'city']

admin.site.register(result)