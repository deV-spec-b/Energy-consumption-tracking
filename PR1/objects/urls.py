from django.urls import path

from . import views

urlpatterns = [
    path("", views.objects_list, name="objects"),
    path("<int:object_id>/", views.object_detail, name="object_detail"),
]
