# inventory_app/views/home.py
from django.shortcuts import render

def home(request):
    return render(request, "base.html")