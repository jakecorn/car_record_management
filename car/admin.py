from django.contrib import admin

# Register your models here.
from .models import Car, CarColor

admin.site.register(Car)
admin.site.register(CarColor)