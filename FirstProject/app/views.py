from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function(request):
    return HttpResponse("Hey this is manoj here")

def testkwrgs(request,**kwrgs):
    name=kwrgs.get("name")
    return HttpResponse(f"<h2>Hey this is to test {name} the kwrgs</h2>")
