from django.db import models

class User(models.Model):

    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    birthDate = models.DateField()
    document = models.CharField(max_length=14)
