from django.contrib.auth.models import AbstractUser
from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField()


class Type(models.Model):
    job = models.ForeignKey(Job, on_delete=models.RESTRICT)
    name = models.CharField(max_length=20)
    img = models.ImageField()


class User(AbstractUser):
    type = models.ForeignKey(Type, on_delete=models.RESTRICT)
    price = models.IntegerField()
    img = models.ImageField(upload_to='uploads')
    comment = models.TextField()
    date_post = models.DateField()

