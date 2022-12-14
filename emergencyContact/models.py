from django.db import models
from police.models import Police

# Create your models here.
class EmergencyContact(models.Model):
    emergency_contact_number=models.IntegerField(primary_key=True)
    emergency_contact_type = models.CharField(max_length=20)
    emergency_contact_place = models.CharField(max_length=20)
    police = models.ForeignKey(Police, on_delete=models.CASCADE)