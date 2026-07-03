from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    grade = models.IntegerField()
    


    def __str__(self):
        return self.name
