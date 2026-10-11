from datetime import date

from models.meters import create_meter
from models.objects import create_object
from models.readings import (
    calculate_consumption,
    create_reading,
    filter_readings_by_meter
)


def _prepare_meter():
    objects: list = []
    meters: list = []
    accounting_object = create_object(objects, "A", "квартира", 20.0)
    meter = create_meter(meters, "ЭЛ-1", "электроэнергия", accounting_object)
    return meter


def test_create_reading() -> None:
    readings: list = []
    meter = _prepare_meter()
    reading = create_reading(
        readings,
        meter,
        1200.0,
        date(2026, 8, 1)
    )
    assert reading.id == 1
    assert reading.value == 1200.0
    assert reading.meter.number == "ЭЛ-1"


def test_filter_readings_by_meter() -> None:
    readings: list = []
    meter = _prepare_meter()
    create_reading(readings, meter, 100.0, date(2026, 8, 1))
    found = filter_readings_by_meter(readings, meter.id)
    assert len(found) == 1


def test_calculate_consumption() -> None:
    readings: list = []
    meter = _prepare_meter()
    create_reading(readings, meter, 1200.0, date(2026, 8, 1))
    create_reading(readings, meter, 1285.5, date(2026, 9, 1))
    consumption = calculate_consumption(readings, meter.id)
    assert consumption == 85.5


def test_calculate_consumption_not_enough() -> None:
    readings: list = []
    meter = _prepare_meter()
    create_reading(readings, meter, 1200.0, date(2026, 8, 1))
    assert calculate_consumption(readings, meter.id) is None
