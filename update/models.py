from django.db import models
from firRegistration.models import FirRegistration

# Create your models here.
class update(models.Model):
    update_id=models.IntegerField(primary_key=True)
    update_time=models.TimeField(max_length=20)
    fir_id = models.ForeignKey(FirRegistration, on_delete=models.CASCADE)
