from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "customer",
            "make",
            "model",
            "year",
            "vin_or_id",
            "status",
        ]
