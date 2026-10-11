from django.urls import path

from . import views

urlpatterns = [
    path("", views.readings_list, name="readings"),
    path(
        "<int:reading_id>/",
        views.reading_detail,
        name="reading_detail",
    ),
]
