
import datetime
from typing import Optional
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.db.models.fields import BigIntegerField
from django.core.files.storage import default_storage
from django.db.models.signals import post_delete
from django.dispatch import receiver
import uuid


class MyAccountManager(BaseUserManager):

    def create_user(self, facebook_id, email, name, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            facebook_id=facebook_id,
            email=self.normalize_email(email),
            name=name,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, facebook_id, email, name, **extra_fields):
        user = self.create_user(
            facebook_id=facebook_id,
            email=self.normalize_email(email),
            name=name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_upload_path(self, filename):
    return 'images/{0}/{1}'.format(self.user.facebook_id, filename)


class Account(AbstractBaseUser, PermissionsMixin):
    facebook_id = models.BigIntegerField(unique=True, primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=300, null=False, blank=False)
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
    profile_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    image = models.FileField(
        upload_to=get_upload_path, null=True, verbose_name="")
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    university_name = models.CharField(max_length=500, null=False, blank=False)
    university_image = models.CharField(
        max_length=10000, null=False, blank=True)
    university_latitude = models.FloatField()
    university_longitude = models.FloatField()
    birth_date = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    personal_description = models.CharField(max_length=1000)
    city = models.CharField(max_length=200, null=False, blank=False)
    course = models.CharField(max_length=1000, null=False, blank=False)
    admission = models.CharField(max_length=300, null=False, blank=False)
    flat_finder = models.CharField(max_length=100, null=False, blank=False)
    sharing_preferences = models.CharField(
        max_length=40, null=False, blank=False)
    food_preferences = models.CharField(
        max_length=100, null=False, blank=False)
    cooking_skills = models.CharField(max_length=300, null=False, blank=False)
    personality = models.CharField(max_length=20000)
