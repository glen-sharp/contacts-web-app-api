from django.db import models


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_number = models.BigIntegerField()
