from django.core.validators import MinValueValidator
from django.db import models





class Person(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    job = models.CharField(max_length=50)
    accepted = models.DateField()
    salary = models.IntegerField(validators=MinValueValidator(0))
    photo = models.ImageField(blank=True, upload_to='media/')
    def __str__(self):
        return self.name, self.job





