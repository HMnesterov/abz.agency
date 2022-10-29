from django.db import models



class Job(models.Model):
    name = models.CharField(50)
    text = models.TextField(1000, blank=True)

class Person(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    patronymic = models.CharField(max_length=40)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    accepted = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name, self.job

class Leader(models.Model):
    owner = models.OneToOneField(Person, on_delete=models.CASCADE, blank=True)
    myself = models.OneToOneField(Person, on_delete=models.CASCADE)
    slaves = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True)





