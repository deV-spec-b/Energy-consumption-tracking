from django.http import HttpResponse

from homepage.views import page
from models.meters import filter_meters_by_object
from models.objects import find_object_by_id
from storage import load_meters, load_objects


def objects_list(request):
    items = ""
    for accounting_object in load_objects("data/objects.json"):
        text = (
            f"{accounting_object.address} – "
            f"{accounting_object.object_type}, "
            f"{accounting_object.area} м²"
        )
        items += (
            f'<li class="list-group-item">'
            f'<a href="/objects/{accounting_object.id}/">{text}</a>'
            f"</li>"
        )
    content = f"""
    <h1>Объекты</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Объекты", content))


def object_detail(request, object_id):
    objects_list_data = load_objects("data/objects.json")
    accounting_object = find_object_by_id(objects_list_data, object_id)
    if accounting_object is None:
        content = """
        <h1 class="text-danger">Объект не найден</h1>
        <a href="/objects/" class="btn btn-outline-secondary">
            ← к списку объектов
        </a>
        """
        return HttpResponse(
            page("Объект не найден", content),
            status=404,
        )
    meters = filter_meters_by_object(
        load_meters("data/meters.json", objects_list_data),
        accounting_object.id,
    )
    meter_items = ""
    for meter in meters:
        meter_items += (
            f'<li class="list-group-item">'
            f'<a href="/meters/{meter.id}/">'
            f"{meter.number} – {meter.meter_type}"
            f"</a></li>"
        )
    if not meter_items:
        meter_items = '<li class="list-group-item">Счётчиков нет</li>'
    content = f"""
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">{accounting_object.address}</h5>
            <p class="card-text">
                <strong>ID:</strong> {accounting_object.id}
            </p>
            <p class="card-text">
                <strong>Тип:</strong> {accounting_object.object_type}
            </p>
            <p class="card-text">
                <strong>Площадь:</strong> {accounting_object.area} м²
            </p>
            <p class="card-text"><strong>Счётчики:</strong></p>
            <ul class="list-group mb-3">{meter_items}</ul>
            <a href="/objects/" class="btn btn-outline-secondary">
                ← к списку объектов
            </a>
        </div>
    </div>
    """
    return HttpResponse(
        page(accounting_object.address, content),
        status=200,
    )
