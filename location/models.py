from django.db import models
from police.models import Police

# Create your models here.
class Location(models.Model):
    location_name=models.CharField(max_length=20)
    police=models.ForeignKey(Police,on_delete=models.CASCADE)
