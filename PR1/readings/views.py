from django.shortcuts import render

from models.readings import find_reading_by_id
from storage import load_meters, load_objects, load_readings


def readings_list(request):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    readings_list = load_readings("data/readings.json", meters_list)
    context = {
        "readings": readings_list,
    }
    return render(request, "readings/reading_list.html", context)


def reading_detail(request, reading_id):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    readings_list = load_readings("data/readings.json", meters_list)
    reading = find_reading_by_id(readings_list, reading_id)
    context = {
        "reading": reading,
    }
    return render(
        request,
        "readings/reading_detail.html",
        context,
        status=404 if reading is None else 200,
    )