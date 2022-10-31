from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
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
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.level > 5:
            try:
               nach = self.parent.level
               self.level = nach - 1 if nach >= 2 else 1
            except Exception:
                self.level = 5
        super().save(*args, **kwargs)

    def get_link(self):
        return reverse('employee', args=[self.pk])

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f"{self.name, self.level}"
