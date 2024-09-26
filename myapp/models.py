from django.db import models

# Create your models here.

class Car(models.Model):
    CarBrand_name=models.CharField(max_length=200)
    Car_speed=models.IntegerField(default=50)

    def __str__(self):
        return self.CarBrand_name
     


