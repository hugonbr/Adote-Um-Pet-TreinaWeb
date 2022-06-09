from django.urls import path

from adocao import views

urlpatterns = [path("", views.AdocaoList.as_view(), name="adocao-list")]
