# myapp/models.py
from django.db import models


class RandomNumber(models.Model):
    value = models.IntegerField()
