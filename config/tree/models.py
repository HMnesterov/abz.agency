from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Person(MPTTModel):
    """Employee model"""
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    job = models.CharField(max_length=50)
    accepted = models.DateField()
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    photo = models.ImageField(blank=True, upload_to='media/', verbose_name='Employee photo')
    chief = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name, self.job
