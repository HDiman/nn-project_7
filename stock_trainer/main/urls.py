from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('zero', views.begin, name="zero"),
]
