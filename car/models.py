from django.db import models

# Create your models here.
from django.db.models import Max
import ast


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.ForeignKey('CarColor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def add_sequence(self, sequence_list):
        self.sequence = sequence_list.index(self.id) + 1
        return self

    def save(self, *args, **kwargs):
        has_id = self.id
        super(Car, self).save(*args, **kwargs)
        if not has_id:
            sequence = CarSequence.objects.all()[0]
            sequence.add_sequence(self.id)

    def car_custom_sort(cars):
        sequence = CarSequence.objects.all()[0]
        sequence_list = sequence.get_list()
        record_list = []

        for car in cars:
            car = car.add_sequence(sequence_list)
            record_list.append(car)

        return sorted(record_list, key=lambda c: sequence_list.index(c.pk))

class CarColor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarSequence(models.Model):
    list = models.TextField(default="[]")

    def add_sequence(self, car_id):
        """
            This function inserts a new element at the last part of the list

            Parameters:
            car_id (int): The primary key from the Car model to be added
        """
        current_list = self.get_list()
        current_list.append(car_id)
        self.list = current_list
        self.save()

    def update_sequence(self, based_car_id, moved_car_id):
        """
            This function changes the order of the elements in the list and save the new order

            Parameters:
            based_car_id (int): The primary key from the Car model where the car to be moved is dropped into
            moved_car_id (int): The primary key from the Car model to be moved to other row
        """
        based_car_id = int(based_car_id)
        moved_car_id = int(moved_car_id)
        current_list = self.get_list()
        based_car_id_position = current_list.index(based_car_id)
        moved_car_id_position = current_list.index(moved_car_id)
        current_list.remove(moved_car_id)
        current_list.insert(based_car_id_position, moved_car_id)
        self.list = current_list
        self.save()

    def delete_item(self, car_id):
        """
            This function removes an element from the list

            Parameters:
            car_id (int): The primary key from the Car model to be deleted in the list
        """
        current_list = self.get_list()
        current_list.remove(car_id)
        self.list = current_list
        self.save()

    def get_list(self):
        """
            Converts the list formatted string to List object

            Returns:
            List object
        """
        return ast.literal_eval(self.list)