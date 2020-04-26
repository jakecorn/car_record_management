from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CarForm
from .models import Car, CarColor


def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        form.save()
        messages.info(request, "The record has  been created")
        return redirect('list_car')
    else:
        form = CarForm(None)
    return render(request, "create_car.html", {'form': form})

def list_car(request):
    # if request.method == "POST":
    # else:
    colors = CarColor.objects.all()
    if 'color' in request.GET:
        cars = Car.objects.filter(color__name__exact=request.GET['color'])
        return render(request, "includes/list_snippet.html", {'cars': cars, 'colors': cars})
    else:
        cars = Car.objects.all()

    return render(request, "list_car.html", {'cars': cars, 'colors': colors})

def delete_car(request, id):
    car = Car.objects.get(id=id)
    if car:
        car.delete()
        messages.info(request, car.name + "  record was deleted")
    else:
        messages.info(request, "The record you are trying to delete is not found in the records")
    return redirect('list_car')

def update_car(request, id):
    form = Car.objects.get(id=id)
    if form:
        if request.method == "POST":
            form = CarForm(request.POST, instance=form)
            form.save()
            messages.info(request, "Record was successfully update")
            return redirect('list_car')
        else:
            form = CarForm(instance=form)
    else:
        messages.info(request, "The record you are trying to delete is not found in the records")
        return redirect('list_car')

    return render(request, "create_car.html", {'form': form})
