from django.db import models

class Unitconv(models.Model):
    fromUnits = models.CharField(max_length=200)
    toUnits = models.CharField(max_length=200)
    conversion = models.FloatField()


