from django.shortcuts import render

# Create your views here.
# landing/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'landing/_index.html')
