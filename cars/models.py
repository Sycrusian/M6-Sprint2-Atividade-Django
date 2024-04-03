from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    is_available = models.BooleanField(default=True)
