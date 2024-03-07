from django.db import models

# Create your models here.

class Food(models.Model):
    fname = models.CharField(max_length = 100)
    frating = models.PositiveIntegerField()
    fprice = models.PositiveIntegerField()


