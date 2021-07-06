
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [

    path('profile/', views.CreateProfile.as_view(), name="create-profile"),
    path('login/', views.CreateAccount.as_view(), name="create-account"),
    path('profile_view/', views.ProfileView.as_view(), name="profile-view")
]
