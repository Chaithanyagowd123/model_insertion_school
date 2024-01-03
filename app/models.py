from django.db import models

# Create your models here.
class create_school(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    slocation=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)