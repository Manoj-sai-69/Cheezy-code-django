from django.shortcuts import render
from students.models import Student

# Create your views here.
def all_students(req):
    students=Student.objects.all()
    print(students)
    context={
        "students":students
    }
    return render(req,'students/students1.html',context=context)


def student(req):
    student=Student.objects.get(name="manoj sai")
    return render(req,'students/students2.html',{'student':student})