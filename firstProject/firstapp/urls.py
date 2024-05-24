from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.topics, name="topics"),
    path("all-chai/", views.chais, name="chais"),
]