from django.shortcuts import render
from .models import Portfolio
import random
import math


# Create your views here.


def index(request):
    return render(request, 'main/index.html')
