from django.urls import  path
from API.views import UserRegistrationView


urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),

]