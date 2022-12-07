from django.contrib import admin
from django.urls import path
from DjangoValidAPP import views

urlpatterns = [
    path('reg/',views.index),
    path('sign/',views.sign)
]
