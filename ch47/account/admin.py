from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user
# Register your models here.


class UserModelAdmin(UserAdmin):
  model = user
  list_display = ['id','name', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller', 'created_at', 'updated_at',]

  list_filter =  ["is_superuser"]

  fieldsets = [
    ('credential info', {'fields': ['email', 'password']}),
    ('persnal Inof', {'fields': ['name','city']}),
    ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller']}),
    ('Important dates', {'fields': ['created_at', 'updated_at']})
  ]

  add_fieldsets = [
    (None, {
      'classes': ['wide'],
      'fields': ['email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller']
    })
  ]

  search_fields = ['name', 'email']
  ordering = ('created_at',)
  filter_horizontal = []

admin.site.register(user, UserModelAdmin)