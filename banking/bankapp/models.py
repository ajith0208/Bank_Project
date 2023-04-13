from django.db import models

# Create your models here.
from django.urls import reverse


class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.name)


class Branch(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account = models.CharField(max_length=100)
    materials = models.TextField()

    def __str__(self):
        return self.name
