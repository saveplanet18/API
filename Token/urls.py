from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import UserProfileListCreateView, userProfileDetailView


urlpatterns = [
    path("allprofiles/",UserProfileListCreateView.as_view(),name="allprofiles"),
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
    path('api-token-auth/', views.obtain_auth_token)
]


