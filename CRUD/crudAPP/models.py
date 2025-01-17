from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):
    """
    the primary user model for CRUD app and
    override it from base User model
    """
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    mobile = models.CharField(max_length=20, unique=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        """
        check if user has perm permission
        """
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        check if user has perm permission for app
        """
        return True
