from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.

def index(request):
	return render(request,'APP1/prueba1.html')