from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField()


class Type(models.Model):
    job = models.ForeignKey(Job, on_delete=models.RESTRICT)
    name = models.CharField(max_length=20)
    img = models.ImageField()


class Skills(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)