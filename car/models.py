from django.db import models

# Create your models here.
from django.db.models import Max


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey('CarColor', on_delete=models.CASCADE)
    sequence = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # here must to find the last order then sum one and save the result
            car = Car.objects.all().aggregate(Max('sequence'))
            print(car)
            if  car['sequence__max'] is not None:
                print(car)
                self.sequence = car['sequence__max'] + 1
        super(Car, self).save(*args, **kwargs)

class CarColor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
