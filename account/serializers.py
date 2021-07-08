from re import A, S
from django.db import models
from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
import datetime
from account.models import Account, Profile


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['facebook_id', 'email', 'name']


class ProfileViewSerializer(serializers.ModelSerializer):
    facebook_id = serializers.SerializerMethodField(
        'get_facebook_id_from_account')
    email = serializers.SerializerMethodField('get_email_from_account')
    name = serializers.SerializerMethodField('get_name_from_account')
    # image = serializers.SerializerMethodField('get_image_from_account')

    class Meta:
        model = Profile
        fields = ['facebook_id', 'email', 'name', 'profile_id', 'image', 'birth_date', 'age', 'gender', 'city', 'course', 'admission',
                  'personal_description', 'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality', 'university_name', 'university_image', 'university_latitude', 'university_longitude']

    def get_facebook_id_from_account(self, profile):
        return profile.user.facebook_id

    def get_email_from_account(self, profile):
        return profile.user.email

    def get_name_from_account(self, profile):
        return profile.user.name


class ProfileCreateSerializer(serializers.ModelSerializer):

    facebook_id = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Account.objects.all())

    class Meta:
        model = Profile
        fields = ['facebook_id', 'birth_date', 'age', 'gender', 'city', 'course', 'admission', 'personal_description',
                  'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality', 'university_name', 'university_image', 'university_latitude', 'university_longitude']
