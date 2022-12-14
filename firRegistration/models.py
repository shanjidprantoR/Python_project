from django.db import models
from userProfile.models import User_profile

# Create your models here.
class FirRegistration(models.Model):
    fir_id=models.IntegerField(primary_key=True)
    fir_date=models.DateField(max_length=20)
    fir_type = models.DateField(max_length=20)
    userProfile = models.ForeignKey(User_profile, on_delete=models.CASCADE)
