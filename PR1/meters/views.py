from django.shortcuts import render

from models.meters import find_meter_by_id
from models.readings import calculate_consumption, filter_readings_by_meter
from storage import load_meters, load_objects, load_readings


def meters_list(request):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    context = {
        "meters": meters_list,
    }
    return render(request, "meters/meter_list.html", context)


def meter_detail(request, meter_id):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    meter = find_meter_by_id(meters_list, meter_id)
    consumption = None
    if meter is not None:
        readings = load_readings("data/readings.json", meters_list)
        meter_readings = filter_readings_by_meter(readings, meter.id)
        consumption = calculate_consumption(meter_readings, meter.id)
    context = {
        "meter": meter,
        "consumption": consumption,
    }
    return render(
        request,
        "meters/meter_detail.html",
        context,
        status=404 if meter is None else 200,
    )