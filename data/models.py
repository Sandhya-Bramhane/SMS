from django.db import models

# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    pass1=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)

class Admin(models.Model):
    email=models.CharField(max_length=20)
    pass1=models.CharField(max_length=20)

class Student(models.Model):
    sname=models.CharField(max_length=20)
    slname=models.CharField(max_length=20)
    sadd=models.CharField(max_length=20)
    sgen=models.CharField(max_length=20)
    sstate=models.CharField(max_length=20)
    scity=models.CharField(max_length=20)
    sdob=models.CharField(max_length=20)
    scor=models.CharField(max_length=20)
    semid=models.CharField(max_length=20)

class Notice(models.Model):
    nid=models.IntegerField()
    dt=models.CharField(max_length=20)
    sub=models.CharField(max_length=100)
    dept=models.CharField(max_length=20)


class Hostel(models.Model):
    sid=models.IntegerField()
    dt=models.CharField(max_length=20)
    fn=models.CharField(max_length=100)
    ln=models.CharField(max_length=20)
    mo=models.CharField(max_length=20)
    co=models.CharField(max_length=20)
    dept=models.CharField(max_length=20)
    du=models.CharField(max_length=20)
    action=models.CharField(max_length=20)


    