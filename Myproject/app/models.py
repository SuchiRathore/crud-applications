from django.db import models

# Create your models here.

class User (models.model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length =200)
    phone = models.IntegerField()
    password = models.CharField(max_length =255)

    
