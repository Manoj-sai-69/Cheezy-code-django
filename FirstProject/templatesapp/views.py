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


def rederhtml(request):
    return render(request,'templatesapp/index.html')

