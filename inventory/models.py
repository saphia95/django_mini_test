from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.

def validate_number_of_digits(value):
    if len(str(value)) != 13:
        raise ValidationError("GTIN contains exactly 13 digits")


class Inventory(models.Model):
    name = models.CharField(default="test", max_length=200)
    gtin = models.BigIntegerField(default=0, validators=[validate_number_of_digits])
    expiry_date = models.DateField('expiry date')
    image_url = models.TextField(default=None, null=True)

    def __str__(self):
        return self.name

    def is_outdated(self):
        return self.expiry_date <= timezone.now().date()

    def get_expiry_date(self):
        return self.expiry_date
        
    def get_gtin(self):
        return self.gtin

    def get_image_url(self):
        return self.image_url
