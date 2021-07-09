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

    def save(self):
        account = Account.objects.create_user(
            email=self.validated_data['email'],
            facebook_id=self.validated_data['facebook_id'],
            name=self.validated_data['name']
        )
        return account


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
        fields = ['facebook_id', 'birth_date', 'image', 'age', 'gender', 'city', 'course', 'admission', 'personal_description',
                  'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality', 'university_name', 'university_image', 'university_latitude', 'university_longitude']

    def save(self):
        profile = Profile.objects.create(
            user=self.validated_data['facebook_id'],
            image=self.validated_data['image'],
            university_name=self.validated_data['university_name'],
            university_image=self.validated_data['university_image'],
            university_latitude=self.validated_data['university_latitude'],
            university_longitude=self.validated_data['university_longitude'],
            birth_date=self.validated_data['birth_date'],
            age=self.validated_data['age'],
            gender=self.validated_data['gender'],
            personal_description=self.validated_data['personal_description'],
            city=self.validated_data['city'],
            course=self.validated_data['course'],
            admission=self.validated_data['admission'],
            flat_finder=self.validated_data['flat_finder'],
            sharing_preferences=self.validated_data['sharing_preferences'],
            food_preferences=self.validated_data['food_preferences'],
            cooking_skills=self.validated_data['cooking_skills'],
            personality=self.validated_data['personality'],
        )
        return profile
