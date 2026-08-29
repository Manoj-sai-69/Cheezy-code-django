from django.shortcuts import render

# Create your views here.
def serverhtml(request):
    return render(request,'staticfilesapp/django.html')