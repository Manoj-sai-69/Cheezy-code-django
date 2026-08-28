from django.urls import path
from .views import rederhtml,filterhtml
urlpatterns=[
    path('',rederhtml),
    path('if/',filterhtml)
]