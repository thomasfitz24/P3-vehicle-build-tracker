from django.contrib import admin
from django.urls import path, include
from builds import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Main app URLs
    path("", views.vehicle_list, name="vehicle_list"),
    path("vehicles/add/", views.vehicle_create, name="vehicle_create"),
    path("vehicles/<int:pk>/edit/", views.vehicle_update, name="vehicle_update"),
    path("vehicles/<int:pk>/", views.vehicle_detail, name="vehicle_detail"),
    path("vehicles/<int:pk>/delete/", views.vehicle_delete, name="vehicle_delete"),
    # Stage URLs
    path(
        "vehicles/<int:vehicle_pk>/stages/add/", views.stage_create, name="stage_create"
    ),
    path("vehicles/stages/<int:pk>/edit/", views.stage_update, name="stage_update"),
    path("vehicles/stages/<int:pk>/delete/", views.stage_delete, name="stage_delete"),
    # Authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),
]
