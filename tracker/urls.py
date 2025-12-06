from django.contrib import admin
from django.urls import path
from builds.views import vehicle_list, vehicle_detail, vehicle_create, vehicle_update, vehicle_delete, stage_create, stage_delete, stage_update

"""
URL configuration for tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", vehicle_list, name="vehicle_list"),
    path("vehicles/add/", vehicle_create, name="vehicle_create"),
    path("vehicles/<int:pk>/edit/", vehicle_update, name="vehicle_update"),
    path("vehicles/<int:pk>/", vehicle_detail, name="vehicle_detail"),
    path("vehicles/<int:pk>/delete/", vehicle_delete, name="vehicle_delete"),
    path("vehicles/<int:vehicle_pk>/stages/add/", stage_create, name="stage_create"),
    path("vehicles/stages/<int:pk>/edit/", stage_update, name="stage_update"),
    path("vehicles/stages/<int:pk>/delete/", stage_delete, name="stage_delete"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("builds.urls")),
]
