from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=("id","name","reg_no","section","mobile")

# Register your models here.
admin.site.register(Student,admin_class=StudentAdmin)
