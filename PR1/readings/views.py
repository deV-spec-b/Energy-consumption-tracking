from django.http import HttpResponse

from homepage.views import page
from models.readings import find_reading_by_id
from storage import load_meters, load_objects, load_readings


def readings_list(request):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    items = ""
    for reading in load_readings("data/readings.json", meters_list):
        text = (
            f"{reading.meter.number} – {reading.reading_date}: "
            f"{reading.value}"
        )
        items += (
            f'<li class="list-group-item">'
            f'<a href="/readings/{reading.id}/">{text}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Показания</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Показания", content))


def reading_detail(request, reading_id):
    objects_list = load_objects("data/objects.json")
    meters_list = load_meters("data/meters.json", objects_list)
    readings = load_readings("data/readings.json", meters_list)
    reading = find_reading_by_id(readings, reading_id)
    if reading is None:
        content = """
        <h1 class="text-danger">Показание не найдено</h1>
        <a href="/readings/" class="btn btn-outline-secondary">
            ← к списку показаний
        </a>
        """
        return HttpResponse(
            page("Показание не найдено", content),
            status=404,
        )
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Показание №{reading.id}</h5>
            <p class="card-text">
                Счётчик:
                <a href="/meters/{reading.meter.id}/">
                    {reading.meter.number}
                </a>
            </p>
            <p class="card-text">Значение: {reading.value}</p>
            <p class="card-text">Дата: {reading.reading_date}</p>
            <p class="card-text">
                Объект: {reading.meter.accounting_object.address}
            </p>
            <a href="/readings/" class="btn btn-outline-secondary">
                ← к списку показаний
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(f"Показание №{reading.id}", content),
        status=200,
    )
