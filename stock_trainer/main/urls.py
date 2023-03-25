from django.urls import path
from . import views
from .views import get_data


urlpatterns = [
    path('', views.index, name="home"),
    path('zero', views.zero_btn, name="zero"),
    path('equalize', views.equalize_btn, name="equalize"),
    path('auto', views.auto_btn, name="auto"),
    path('get-data/', get_data, name='get-data'),
]
