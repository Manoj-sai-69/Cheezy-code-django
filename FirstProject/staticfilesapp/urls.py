from django.urls import path
from staticfilesapp.views import serverhtml

urlpatterns=[
    path('',serverhtml)
]