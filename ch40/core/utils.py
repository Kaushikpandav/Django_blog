from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .permission_config import PERMISSION_CONFIG

def assign_permission(user, role):
  permission_role = PERMISSION_CONFIG.get(role, {})

  for model, permissions in permission_role.items():
    try:
        content_type = ContentType.objects.get_for_model(model)
        for permission_name in permissions:
            codename = f"{permission_name}_{model._meta.model_name}"
            try:
                permission = Permission.objects.get(codename=codename, content_type=content_type)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                print(f"Warning: Permission {codename} not found for {model._meta.model_name}")
    except Exception as e:
        print(f"Error assigning permissions for model {model}: {e}")