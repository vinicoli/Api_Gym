"""
Database models.
"""
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.CharField(max_length=100, blank=True)
    data_de_nascimento = models.DateField(null=True, blank=False)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], null=True, blank=True)
    endereco_rua = models.CharField(max_length=100, blank=True)
    endereco_cidade = models.CharField(max_length=100, blank=True)
    endereco_estado = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50, blank=True)



