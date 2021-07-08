from datetime import date
import json
from os import stat
from django.db.models.expressions import RawSQL
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from account.models import Account, Profile
from account.serializers import AccountSerializer, ProfileCreateSerializer, ProfileViewSerializer


class CreateAccount(APIView):

    def post(self, request, *args, **kwargs):
        form = request.data
        if not(form.__contains__("facebook_id")):
            return JsonResponse({"success": False, "message": "Please do pass the facebook_id as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["facebook_id"] == "":
            return JsonResponse({"success": False, "response": "please login first"}, status=status.HTTP_400_BAD_REQUEST)
        elif Account.objects.filter(facebook_id=form['facebook_id']).exists():
            return JsonResponse({"success": False, "response": "facebook id already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("email")):
            return JsonResponse({"success": False, "message": "Please pass a valid email as it is required"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["email"] == "":
            return JsonResponse({"success": False, "response": "please login first"}, status=status.HTTP_400_BAD_REQUEST)
        elif Account.objects.filter(email=form['email']).exists():
            return JsonResponse({"success": False, "response": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("name")):
            return JsonResponse({"success": False, "message": "PLease enter your name as it is necessary "}, status=status.HTTP_400_BAD_REQUEST)
        elif form["name"] == "":
            return JsonResponse({"success": False, "response": "please enter a valid name"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AccountSerializer(data=form)
        if serializer.is_valid(raise_exception=True):
            account = serializer.save()
            data = {
                "success": True,
                "account": account,
            }
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "success": False
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


class ViewAccount(APIView):

    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class CreateProfile(APIView):

    def post(self, request, *args, **kwargs):
        form = request.data

        if not(form.__contains__("facebook_id")):
            return JsonResponse({"success": False, "message": "Please login first"}, status=status.HTTP_400_BAD_REQUEST)
        elif form['facebook_id'] == "":
            return JsonResponse({"success": False, "message": "Please login first"}, status=status.HTTP_400_BAD_REQUEST)
        elif Profile.objects.filter(user=form['facebook_id']).exists():
            return JsonResponse({"success": False, "response": "profile already added"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("gender")):
            return JsonResponse({"success": False, "message": "Please enter the gender as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form['gender'] == "" or not(form['gender'] == 'Male' or form['gender'] == 'Female' or form['gender'] == 'Non-Binary'):
            return JsonResponse(
                {"success": False, "reponse": "Gender is a compulsory field and enter a valid gender"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("city")):
            return JsonResponse({"success": False, "message": "Please enter the proper city as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["city"] == "":
            return JsonResponse(
                {"success": False, "reponse": "City is a compulsory field"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("course")):
            return JsonResponse({"success": False, "message": "Please enter the course as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["course"] == "":
            return JsonResponse(
                {"success": False, "response": "Course is a compulsory field"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("admission")):
            return JsonResponse({"success": False, "message": "Please enter the admission details as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["admission"] == "":
            return JsonResponse({"success": False, "response": "Admission is a compulsory field"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("flat_finder")):
            return JsonResponse({"success": False, "message": "Please enter a valid data related to finding a flat as it is required"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["flat_finder"] == "":
            return JsonResponse({"success": False, "response": "Flat finding details are essential"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("sharing_preferences")):
            return JsonResponse({"success": False, "message": "Please enter the sharing preferences as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["sharing_preferences"] == "":
            return JsonResponse({"success": False, "response": "Sharing Preferences are essential"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("food_preferences")):
            return JsonResponse({"success": False, "message": "Please enter the food preferences as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["food_preferences"] == "":
            return JsonResponse({"success": False, "response": "Food prefernce is an essential field"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("cooking_skills")):
            return JsonResponse({"success": False, "message": "Please enter the cooking skills as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["cooking_skills"] == "":
            return JsonResponse({"success": False, "response": "cooking skills are essential"}, status=status.HTTP_400_BAD_REQUEST)

        if not(form.__contains__("university")):
            return JsonResponse({"success": False, "message": "Please enter the university as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        elif form["university"] == "":
            if form['university']["name"] == "":
                return JsonResponse({"success": False, "response": "university name is an essential field and can't be null"}, status=status.HTTP_400_BAD_REQUEST)
            if form['university']["photo"] == "":
                return JsonResponse({"success": False, "response": "university name is an essential field and can't be null"}, status=status.HTTP_400_BAD_REQUEST)
            if form['university']["latitude"] == "":
                return JsonResponse({"success": False, "response": "university latitude is an essential field and can't be null"}, status=status.HTTP_400_BAD_REQUEST)
            if form['university']["longitude"] == "":
                return JsonResponse({"success": False, "response": "university longitude is an essential field and can't be null"}, status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse({"success": False, "response": "please choose a valid university"}, status=status.HTTP_400_BAD_REQUEST)

        form["university_name"] = form["university"]["name"]
        form["university_image"] = form["university"]["photo"]
        form["university_latitude"] = form["university"]["latitude"]
        form["university_longitude"] = form["university"]["longitude"]
        serializer = ProfileCreateSerializer(data=form)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            data = {
                "succes": True,
                "user": user,
            }
            return JsonResponse(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                "success": False
            }
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=kwargs['id'])
        except Profile.DoesNotExist:
            return JsonResponse({"success": False, "message": "The given profile does not exist"})
        serializer = ProfileViewSerializer(profile)
        new_data = {
            "name": serializer.data["name"],
            "user_id": serializer.data["profile_id"],
            "gender": serializer.data["gender"],
            "dob": serializer.data["birth_date"],
            "age": serializer.data["age"],
            "personal_description": serializer.data["personal_description"],
            "profile_photo": serializer.data["image"],
            "personality": serializer.data['personality'].split(","),
            "city": serializer.data["city"],
            "course": serializer.data["course"],
            "admission": serializer.data["admission"],
            "cooking_skills": serializer.data["cooking_skills"],
            "sharing_preferences": serializer.data["sharing_preferences"],
            "food_preferences": serializer.data["food_preferences"],
            "flat_finder": serializer.data["flat_finder"],
            "prospective_university": {
                "name": serializer.data["university_name"],
                "photo": serializer.data["university_image"],
                "latitude": serializer.data["university_latitude"],
                "longitude": serializer.data["university_longitude"],
            }
        }
        return Response(data=new_data, status=status.HTTP_200_OK)
