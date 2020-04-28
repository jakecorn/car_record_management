from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CarForm
from .models import Car, CarColor, CarSequence


def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        form.save()
        messages.info(request, "The new record has been created")
        return redirect('list_car')
    else:
        form = CarForm(None)
    return render(request, "create_car.html", {'form': form})


def list_car(request):
    colors = CarColor.objects.all()
    if 'color' in request.GET:
        if request.GET['color'] != 'all':
            cars = Car.objects.filter(color__name__exact=request.GET['color'])
        else:
            cars = Car.objects.all()
        cars = Car.car_custom_sort(cars)

        return render(request, "includes/list_snippet.html", {'cars': cars, 'colors': cars})
    else:
        cars = Car.objects.all()
        cars = Car.car_custom_sort(cars)

    return render(request, "list_car.html", {'cars': cars, 'colors': colors})


def delete_car(request, id):
    car = Car.objects.get(id=id)
    if car:
        if car.delete():
            sequence = CarSequence.objects.all()[0]
            sequence.delete_item(id)
            messages.info(request, car.name + "  record was deleted")
        else:
            messages.info(request, "There is a problem in deleting a record.")
    else:
        messages.info(request, "The record you are trying to delete is not found in the database")
    return redirect('list_car')


def update_car(request, id):
    form = Car.objects.get(id=id)
    if form:
        if request.method == "POST":
            form = CarForm(request.POST, instance=form)
            form.save()
            messages.info(request, "The record was successfully updated")
            return redirect('list_car')
        else:
            form = CarForm(instance=form)
    else:
        messages.info(request, "The record you are trying to delete is not found in the database")
        return redirect('list_car')

    return render(request, "create_car.html", {'form': form})


def update_order(request):
    based_car_id = request.GET['based_car_id']
    moved_car_id = request.GET['moved_car_id']
    sequence = CarSequence.objects.all()[0]
    sequence.update_sequence(based_car_id, moved_car_id)

    return redirect('list_car')
