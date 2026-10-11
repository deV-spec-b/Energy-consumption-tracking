from django.urls import path

from . import views

urlpatterns = [
    path("", views.meters_list, name="meters"),
    path("<int:meter_id>/", views.meter_detail, name="meter_detail"),
]
