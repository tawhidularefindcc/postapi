from django.urls import path
from .views import *

urlpatterns = [
    path('users/create', CreateUserView.as_view()),
]
