from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('zero', views.zero_btn, name="zero"),
    path('equalize', views.equalize_btn, name="equalize"),
    path('auto', views.auto_btn, name="auto"),
]
