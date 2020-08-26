from django.db import models
from django.utils import timezone


# Create your models here.

class Inventory(models.Model):
    name = models.CharField(default="test" ,max_length=200)
    gtin = models.BigIntegerField(default = 0)
    expiry_date = models.DateField('expiry date')
    def __str__(self):
        return self.name

    def is_outdated(self):
        return self.expiry_date <= timezone.now().date()

    def get_expiry_date(self):
        return self.expiry_date
        
    def get_gtin(self):
        return self.gtin