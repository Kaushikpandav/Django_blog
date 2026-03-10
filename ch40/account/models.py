from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class usermanager(BaseUserManager):

  def create_user(self,email,password=None):
    if not email:
      raise ValueError("User must have an email address")

    user = self.model(email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,email,password=None, **kwargs):

    kwargs.setdefault('is_superuser',True)
    kwargs.setdefault('is_staff',True)

    if kwargs.get('is_staff') is not True:
      raise ValueError("Superuser must have is_staff=True")

    if kwargs.get('is_superuser') is not True:
      raise ValueError("Superuser must have is_superuser=True")

    user = self.create_user(email=email,password=password)

    user.is_staff = True
    user.is_superuser = True
    user.is_customer = True
    user.is_seller  = True

    user.save(using=self._db)
    return user

# class with custom user model
class user(AbstractBaseUser):
  email = models.EmailField(verbose_name="Email", unique=True)
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  is_active = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_customer = models.BooleanField(default=True)
  is_seller = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'

  REQUIRED_FIELDS = ['name', 'city']

  objects = usermanager()

  def __str__(self):
      return self.email

  def has_perm(self, perm, obj=None):
    """
    Returns True if the user has the given permission. If the user is active and is a
    superuser, this method will always return True.

    :param perm: The permission to check.
    :param obj: The object to check the permission against.
    :return: True if the user has the permission, False otherwise.
    """
    return self.is_superuser

  def has_module_perms(self, app_label):
    """
    Returns True if the user has any permissions in the given app_label.
    If the user is active and is_superuser, this method will always return True.
    """
    return self.is_superuser