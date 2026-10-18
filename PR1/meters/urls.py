from django.urls import path

from . import views

app_name = "meters"

urlpatterns = [
    path("", views.meters_list, name="list"),
    path("<int:meter_id>/", views.meter_detail, name="detail"),
]