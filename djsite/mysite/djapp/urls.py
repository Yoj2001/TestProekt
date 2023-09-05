from django.shortcuts import render
from django.urls import path
from .views import *

app_name = "my_dj"
urlpatterns = [
    path('', index, name="index"),
    path("detail/<int:question_id>", detail, name="detail"),
    path("<int:question_id>/result", result, name="result"),
    path("<int:question_id>/vote", vote, name="vote"),
]