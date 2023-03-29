from django.db import models

# Create your models here.

class mssg(models.Model):
    reciver_no = models.CharField(max_length=13)
    msg = models.CharField(max_length=200)
    hour = models.IntegerField(max_length=24)
    min = models.IntegerField(max_length=60)

