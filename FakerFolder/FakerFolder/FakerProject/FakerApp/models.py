from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

