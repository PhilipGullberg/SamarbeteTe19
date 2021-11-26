from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #Person 5, Här behövs skicka till en view-funktion som heter shop
    path('', views.shop, name="shop"),

]
