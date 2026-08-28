from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

# Create your views here.
def rederhtml(request):
    html='<html lang="en"><head><title>Document</title></head><body><h1>hey hi this is manoj sai</h1></body></html>'
    return HttpResponse(html)

