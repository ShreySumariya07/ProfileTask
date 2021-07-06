
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.fields import BigIntegerField


class MyAccountManager(BaseUserManager):

    def create_user(self, facebook_id, email, name, image, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            facebook_id=facebook_id,
            email=self.normalize_email(email),
            name=name,
            image=image,

        )
        user.save(using=self._db)
        return user

    def create_superuser(self, facebook_id, email, name, image, **extra_fields):
        user = self.create_user(
            facebook_id=facebook_id,
            email=self.normalize_email(email),
            name=name,
            image=image,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    facebook_id = models.BigIntegerField(unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to="media/", null=True, verbose_name="")

    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True


class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    birth_date = models.CharField(max_length=20)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=10)
    personal_description = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    course = models.CharField(max_length=1000)
    admission = models.CharField(max_length=300)
    flat_finder = models.CharField(max_length=100)
    sharing_preferences = models.CharField(max_length=40)
    food_preferences = models.CharField(max_length=100)
    cooking_skills = models.CharField(max_length=300)
    personality = models.CharField(max_length=20000)
