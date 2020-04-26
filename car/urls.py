from . import views
from django.urls import path

urlpatterns = [
    path("car/create", views.create_car, name="create_car"),
    path("car/list", views.list_car, name="list_car"),
    path("car/delete/<int:id>", views.delete_car, name="delete_car"),
    path("car/update/<int:id>", views.update_car, name="update_car"),
    path("car/update/order", views.update_order, name="update_order"),
]