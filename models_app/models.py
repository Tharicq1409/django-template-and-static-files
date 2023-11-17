from django.db import models

# Create your models here.
class customer(models.Model):
    First_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    Email = models.EmailField()