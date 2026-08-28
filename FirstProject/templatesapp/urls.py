from django.urls import path
from .views import rederhtml
urlpatterns=[
    path('',rederhtml)
]