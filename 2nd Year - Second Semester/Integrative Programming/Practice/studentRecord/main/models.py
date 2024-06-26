from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    mobile_num = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    year = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'