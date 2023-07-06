from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=(" first_name", "last_name",  "age",   "nationality",  "code_number")

admin.site.register(Student, StudentAdmin)    

