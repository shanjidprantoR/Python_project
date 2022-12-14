from django.db import models
from user.models import User


# Create your models here.
class Police(models.Model):
    police_id=models.IntegerField(primary_key=True)
    police_station_name=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)