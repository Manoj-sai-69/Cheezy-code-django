from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse



# If your structure is:

# myapp/
#     templates/
#         myapp/
#             home.html
#             login.html
# Then:
# return render(request, 'myapp/home.html')
# NOT
# return render(request, '/templates/myapp/home.html')  # ❌
# and NOT
# return render(request, '/myapp/home.html')  # ❌

from datetime import datetime
def rederhtml(request):
    dt=datetime.now()
    manoj_details={
        "name":"manoj sai",
        "description":"Manoj sai the most worst fellow in whole class",
        "date":dt,
        "age":18
    }
    return render(request,'templatesapp/index.html',context=manoj_details)


def filterhtml(request):
    dic={
        "age":18,
        "gender":"male",
        "eligibility":"You are eligible",
        "voter_lost":["abhi","sais","gans"]
    }
    return render(request,'templatesapp/django.html',context=dic)