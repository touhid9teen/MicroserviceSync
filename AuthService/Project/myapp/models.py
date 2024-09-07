from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, n_id, pin_code,**extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not password:
            raise ValueError('The Phone Number field must be set')
        if not n_id:
            raise ValueError('The National ID (NID) must be set')
        if not pin_code:
            raise ValueError('The Pin Code must be set')    
        
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            n_id = n_id,
            pin_code = pin_code,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True) 
    n_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    pin_code = models.CharField(max_length=6, null=True, blank=True)
    password = models.CharField(max_length=100)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['n_id', 'pin_code']


