from django.db import models


# Create your models here.
class Ambulance(models.Model):
    Name = models.CharField(max_length=50)
    Number = models.CharField(max_length=30)



class Pharmacy(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=20)
    OpeningHour = models.CharField(max_length=20)


class BloodBank(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=50)


class Hospital(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Contact = models.CharField(max_length=20)


class Message(models.Model):
    sender = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
