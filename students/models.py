from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name

