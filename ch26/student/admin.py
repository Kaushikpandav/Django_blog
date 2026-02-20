from django.contrib import admin
from .models import profile, result

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'city']

@admin.register(result)
class resultAdmin(admin.ModelAdmin):
    list_display = ['id', 'st_class', 'st_roll', 'st_marks']

# admin.site.register(result, resultAdmin)
# admin.site.register(profile, profileAdmin)