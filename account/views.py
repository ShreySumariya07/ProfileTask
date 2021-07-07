from datetime import date
import json
from os import stat
from django.db.models.expressions import RawSQL
from django.http.response import JsonResponse
from django.shortcuts import render
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
        if not(form.__contains__("email")):
            return JsonResponse({"success": False, "message": "Please pass a valid email as it is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("name")):
            return JsonResponse({"success": False, "message": "PLease enter your name as it is necessary "}, status=status.HTTP_400_BAD_REQUEST)
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
            return JsonResponse({"success": False, "message": "Please do pass the facebook_id as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("gender")):
            return JsonResponse({"success": False, "message": "Please enter the gender as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("city")):
            return JsonResponse({"success": False, "message": "Please enter the proper city as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("course")):
            return JsonResponse({"success": False, "message": "Please enter the course as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("admission")):
            return JsonResponse({"success": False, "message": "Please enter the admission details as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("flat_finder")):
            return JsonResponse({"success": False, "message": "Please enter a valid data related to finding a flat as it is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("sharing_preferences")):
            return JsonResponse({"success": False, "message": "Please enter the sharing preferences as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("food_preferences")):
            return JsonResponse({"success": False, "message": "Please enter the food preferences as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("cooking_skills")):
            return JsonResponse({"success": False, "message": "Please enter the cooking skills as it is required field"}, status=status.HTTP_400_BAD_REQUEST)
        if not(form.__contains__("university")):
            return JsonResponse({"success": False, "message": "Please enter the university as it is required field"}, status=status.HTTP_400_BAD_REQUEST)

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
        profile = Profile.objects.all()
        serializer = ProfileViewSerializer(profile, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
