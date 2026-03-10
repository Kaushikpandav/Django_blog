from django.contrib import admin
from .models import user
from django.contrib.auth.admin import UserAdmin

# @admin.register(user)
# class userAdmin(admin.ModelAdmin):
#   list_display = ['name', 'email', 'password']

class usermodeladmin(UserAdmin):
  list_display = ['id', 'name', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller', 'created_at', 'updated_at']

  list_filter = ['is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller']

  search_fields = ['name', 'email',  'is_staff', 'is_superuser', 'is_customer', 'is_seller']

  ordering = ('created_at',)

  # update
  fieldsets = [
    ('credential info', {'fields': ['name', 'email', 'password']}),
    ('persnal Inof', {'fields': ['city']}),
    ('Permissions', {'fields': ['is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller']}),
    # ('Important dates', {'fields': ['created_at', 'updated_at']})
  ]

  # adding new user
  add_fieldsets = [
    (None, {
      'classes': ['wide'],
      'fields': ['name', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'is_customer', 'is_seller']
    })
  ]

  filter_horizontal = []

admin.site.register(user, usermodeladmin)