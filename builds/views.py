from django.shortcuts import render
from .models import Vehicle


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "builds/vehicle_list.html", {"vehicles": vehicles})
