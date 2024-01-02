from django.db import models

from django.contrib.auth.models import(
    BaseUserManager,AbstractBaseUser,PermissionsMixin
)
from django.urls import reverse_lazy

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, sex=None, date_of_birth=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email,
            sex=sex,
            date_of_birth=date_of_birth
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class Users(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=255, unique=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse_lazy('accounts:home')
    
    