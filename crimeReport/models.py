from django.db import models
from userProfile.models import User_profile

# Create your models here.
class CrimeReport(models.Model):
    crime_report_type = models.CharField(max_length=20)
    crime_report_place = models.CharField(max_length=20)
    crime_report_name = models.CharField(max_length=20)
    userProfile = models.ForeignKey(User_profile, on_delete=models.CASCADE)
