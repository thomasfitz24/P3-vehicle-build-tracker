from django import forms
from .models import Vehicle, BuildStage


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


class BuildStageForm(forms.ModelForm):
    class Meta:
        model = BuildStage
        fields = [
            "name",
            "description",
            "status",
            "order",
            "due_date",
            "completed_date",
        ]
