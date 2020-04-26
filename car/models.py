from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey('CarColor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CarColor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
