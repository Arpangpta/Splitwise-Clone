from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique = True)
    totalPendingBalance = models.FloatField()

#   To be reviewed
#    associatedGroups = models.ManyToManyField(Group)

class Group(models.Model):
    name = models.CharField(max_length=20)
    member = models.ManyToManyField(Person)
    