from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


class Sports(models.Model):
    Playername = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)