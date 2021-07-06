from datetime import date
from os import stat
from django.db.models.expressions import RawSQL
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.settings import IMPORT_STRINGS
from rest_framework.views import APIView
from account.models import Account, Profile
from account.serializers import AccountSerializer, ProfileCreateSerializer, ProfileViewSerializer


class CreateAccount(APIView):

    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
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


class CreateProfile(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ProfileCreateSerializer(data=request.data)
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
