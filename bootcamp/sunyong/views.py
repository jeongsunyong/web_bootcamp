from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
import openpyxl

def index(request):
    return render(request,'sunyong/home.html')
# Create your views here.

def save_excel(request):
    return render(request,'sunyong/mystorage.html')