from django.urls import path
from students.views import all_students,student

urlpatterns=[
    path('all/',all_students),
    path('student/',student)
]