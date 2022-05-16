from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Type


class User(AbstractUser):
    pass


class TypeUser(models.Model):
    name = models.CharField(max_length=20)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    experiance = models.CharField(max_length=50)
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
    type = models.ManyToManyField(Type)
    price = models.IntegerField()
    old = models.IntegerField()
    img = models.ImageField(upload_to='uploads')
    comment = models.TextField()
    date_post = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    contact = models.URLField()


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    skills = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.RESTRICT)
    img = models.ImageField(upload_to='uploads')
    comment = models.TextField()
    language = models.CharField(max_length=50)
    date_post = models.DateField()
    price = models.IntegerField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.URLField()
