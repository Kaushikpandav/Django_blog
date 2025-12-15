





# Custom user model : it's a way to add extra fields to user model.


Django have 2 class : 

2) AbstractBaseUser : it's a way to create a new user model.

1) AbstractUser : it's a way to add extra fields to user model.

#In modles.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    bio = models.TextField(max_length=50)
    email = models.EmailField(unique=True)
    user_profile = models.ImageField(upload_to='user_profile', default='default.jpg')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

# Now createa manager.py 
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone number must be set')
        extra_fields['email'] = self.normalize_email(extra_fields.get('email'))

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user  

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(phone_number, password, **extra_fields)

# add models in settings.py

AUTH_USER_MODEL = 'Custom_user_model.CustomUser'

# add import in view.py

now in each portion do liek this : "from django.contrib.auth.models import User"  to "from django.contrib.auth import get_user_model"

User = get_user_model()