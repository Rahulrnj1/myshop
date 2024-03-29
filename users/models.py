from typing import Type
from django.db import models

# Create your models here
class Product (models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=150)
    type = models.TextField()
    details = models.TextField()

    def __str__(self) -> str:
        return (self.name)

