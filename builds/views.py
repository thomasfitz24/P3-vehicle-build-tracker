from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, BuildStage
from .forms import VehicleForm, BuildStageForm


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, "builds/vehicle_list.html", {"vehicles": vehicles})


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    stages = vehicle.stages.all()
    context = {
        "vehicle": vehicle,
        "stages": stages,
    }
    return render(request, "builds/vehicle_detail.html", context)

def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vehicle_list")
    else:
        form = VehicleForm()

    return render(request, "builds/vehicle_form.html", {"form": form, "title": "Add Vehicle"})

def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect("vehicle_detail", pk=vehicle.pk)
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, "builds/vehicle_form.html", {"form": form, "title": "Edit Vehicle"})

def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicle_list")
    return render(request, "builds/vehicle_confirm_delete.html", {"vehicle": vehicle})


def stage_create(request, vehicle_pk):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_pk)
    if request.method == "POST":
        form = BuildStageForm(request.POST)
        if form.is_valid():
            stage = form.save(commit=False)
            stage.vehicle = vehicle
            stage.save()
            return redirect("vehicle_detail", pk=vehicle.pk)
    else:
        form = BuildStageForm()

    context = {
        "form": form,
        "vehicle": vehicle,
        "title": "Add Build Stage",
    }
    return render(request, "builds/stage_form.html", context)
