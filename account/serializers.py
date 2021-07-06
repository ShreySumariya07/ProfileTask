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
        fields = ['facebook_id', 'email', 'name', 'image']

    def validate(self, validated_data):
        if Account.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "email already exists"})
        if Account.objects.filter(facebook_id=validated_data['facebook_id']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "facebook id already exists"})
        account = Account.objects.create(
            facebook_id=validated_data["facebook_id"],
            email=validated_data["email"],
            name=validated_data["name"],
            image=validated_data["image"],
        )
        return account


class ProfileViewSerializer(serializers.ModelSerializer):
    facebook_id = serializers.SerializerMethodField(
        'get_facebook_id_from_account')
    email = serializers.SerializerMethodField('get_email_from_account')
    name = serializers.SerializerMethodField('get_name_from_account')

    # image1 = Account.objects.filter(
    #     facebook_id=facebook_id).values_list("image")
    # image = image1

    class Meta:
        model = Profile
        fields = ['facebook_id', 'email', 'name', 'user_id', 'birth_date', 'age', 'gender', 'city', 'course', 'admission',
                  'personal_description', 'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality']

    def get_facebook_id_from_account(self, profile):
        return profile.user.facebook_id

    def get_email_from_account(self, profile):
        return profile.user.email

    def get_name_from_account(self, profile):
        return profile.user.name

    # def get_image_from_account(self, profile):
    #     print(profile.user.image)
    #     return profile.user.image


class ProfileCreateSerializer(serializers.ModelSerializer):

    user_id = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Account.objects.all())

    class Meta:
        model = Profile
        fields = ['user_id', 'birth_date', 'age', 'gender', 'city', 'course', 'admission', 'personal_description',
                  'flat_finder', 'sharing_preferences', 'food_preferences', 'cooking_skills', 'personality']

    def validate(self, validated_data):
        if Profile.objects.filter(user_id=validated_data['user_id'].id).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "profile already added"})
        if validated_data['gender'] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "Gender is a compulsory field"})
        if validated_data["city"] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "City is a compulsory field"})
        if validated_data["admission"] == "":
            raise serializers.ValidationError({
                "success": False, "response": "Admission is a compulsory field"
            })
        if validated_data["course"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Course is a compulsory field"})
        if validated_data["flat_finder"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Flat finding details are essential"})
        if validated_data["sharing_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Sharing Preferences are essential"})
        if validated_data["food_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Food prefernce is an essential field"})
        if validated_data["cooking_skills"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "cooking skills are essential"})

        profile = Profile.objects.create(
            user=validated_data['user_id'],
            birth_date=validated_data['birth_date'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            personal_description=validated_data["personal_description"],
            city=validated_data["city"],
            course=validated_data["course"],
            admission=validated_data["admission"],
            flat_finder=validated_data["flat_finder"],
            sharing_preferences=validated_data["sharing_preferences"],
            food_preferences=validated_data["food_preferences"],
            cooking_skills=validated_data["cooking_skills"],
            personality=validated_data["personality"]
        )

        return profile
