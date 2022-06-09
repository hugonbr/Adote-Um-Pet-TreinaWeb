from django.urls import path

from pet import views

urlpatterns = [path("", views.PetList.as_view(), name="pet-list")]
