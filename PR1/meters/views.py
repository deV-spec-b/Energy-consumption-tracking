from django.http import HttpResponse

from homepage.views import page
from models.meters import find_meter_by_id
from models.readings import (
    calculate_consumption,
    filter_readings_by_meter,
)
from storage import load_meters, load_objects, load_readings


def meters_list(request):
    objects_list = load_objects("data/objects.json")
    items = ""
    for meter in load_meters("data/meters.json", objects_list):
        text = (
            f"{meter.number} – {meter.meter_type}, "
            f"{meter.accounting_object.address}"
        )
        items += (
            f'<li class="list-group-item">'
            f'<a href="/meters/{meter.id}/">{text}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Счётчики</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Счётчики", content))


def meter_detail(request, meter_id):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    meter = find_meter_by_id(meters_list, meter_id)
    if meter is None:
        content = """
        <h1 class="text-danger">Счётчик не найден</h1>
        <a href="/meters/" class="btn btn-outline-secondary">
            ← к списку счётчиков
        </a>
        """
        return HttpResponse(
            page("Счётчик не найден", content),
            status=404,
        )
    readings = load_readings("data/readings.json", meters_list)
    consumption = calculate_consumption(readings, meter.id)
    if consumption is None:
        consumption_text = "недостаточно показаний"
        badge = "bg-secondary"
    else:
        consumption_text = str(consumption)
        badge = "bg-success"
    reading_items = ""
    for reading in filter_readings_by_meter(readings, meter.id):
        reading_items += (
            f'<li class="list-group-item">'
            f'<a href="/readings/{reading.id}/">'
            f"{reading.reading_date}: {reading.value}"
            f"</a></li>"
        )
    if not reading_items:
        reading_items = '<li class="list-group-item">Показаний нет</li>'
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Счётчик {meter.number}</h5>
            <p class="card-text"><strong>ID:</strong> {meter.id}</p>
            <p class="card-text">
                <strong>Тип:</strong> {meter.meter_type}
            </p>
            <p class="card-text">
                <strong>Объект:</strong>
                <a href="/objects/{meter.accounting_object.id}/">
                    {meter.accounting_object.address}
                </a>
            </p>
            <p class="card-text">
                <strong>Статус:</strong> {meter.status}
            </p>
            <p class="card-text">
                Расход по всем показаниям:
                <span class="badge {badge}">{consumption_text}</span>
            </p>
            <p class="card-text"><strong>Показания:</strong></p>
            <ul class="list-group mb-3">{reading_items}</ul>
            <a href="/meters/" class="btn btn-outline-secondary">
                ← к списку счётчиков
            </a>
        </div>
    </div>
    """
    return HttpResponse(page(meter.number, content), status=200)
