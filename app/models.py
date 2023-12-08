from django.db import models

class Country(models.Model):
    country=models.CharField(max_length=100,primary_key=True)

class capital
