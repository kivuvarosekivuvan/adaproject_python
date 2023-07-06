from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    nationality=models.CharField(max_length=30)
    code_number=models.IntegerField()

