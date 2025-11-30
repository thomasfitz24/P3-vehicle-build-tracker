from django.contrib import admin
from .models import Customer, Vehicle, BuildStage


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "vin_or_id", "customer", "status", "created_at")
    list_filter = ("status", "make")
    search_fields = ("make", "model", "vin_or_id", "customer__first_name", "customer__last_name")


@admin.register(BuildStage)
class BuildStageAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "name", "status", "order", "due_date", "completed_date")
    list_filter = ("status",)
    search_fields = ("name", "vehicle__make", "vehicle__model", "vehicle__vin_or_id")
