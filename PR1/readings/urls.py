from django.urls import path

from . import views

app_name = "readings"

urlpatterns = [
    path("", views.readings_list, name="list"),
    path("<int:reading_id>/", views.reading_detail, name="detail"),
]