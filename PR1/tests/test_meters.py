from models.meters import (
    create_meter,
    filter_meters_by_object,
    find_meter_by_id
)
from models.objects import create_object


def test_create_meter() -> None:
    objects: list = []
    meters: list = []
    accounting_object = create_object(
        objects,
        "ул. Ленина, д. 10",
        "квартира",
        50.0
    )
    meter = create_meter(
        meters,
        "ЭЛ-1001",
        "электроэнергия",
        accounting_object
    )
    assert meter.id == 1
    assert meter.number == "ЭЛ-1001"
    assert meter.accounting_object.id == 1
    assert meter.status == "Активен"


def test_find_meter_by_id() -> None:
    objects: list = []
    meters: list = []
    accounting_object = create_object(objects, "A", "квартира", 20.0)
    create_meter(meters, "В-11", "вода", accounting_object)
    meter = find_meter_by_id(meters, 1)
    assert meter is not None
    assert meter.number == "В-11"


def test_filter_meters_by_object() -> None:
    objects: list = []
    meters: list = []
    first = create_object(objects, "A", "квартира", 20.0)
    second = create_object(objects, "B", "офис", 40.0)
    create_meter(meters, "ЭЛ-1", "электроэнергия", first)
    create_meter(meters, "ЭЛ-2", "электроэнергия", second)
    found = filter_meters_by_object(meters, first.id)
    assert len(found) == 1
    assert found[0].number == "ЭЛ-1"


def test_deactivate_meter() -> None:
    objects: list = []
    meters: list = []
    accounting_object = create_object(objects, "A", "квартира", 20.0)
    meter = create_meter(meters, "ЭЛ-1", "электроэнергия", accounting_object)
    meter.deactivate()
    assert meter.status == "Неактивен"
