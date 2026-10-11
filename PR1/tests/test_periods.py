from datetime import date

from models.meters import create_meter
from models.objects import create_object
from models.periods import (
    calculate_period_consumption,
    create_period,
    find_period_by_id
)
from models.readings import create_reading


def test_create_period() -> None:
    periods: list = []
    period = create_period(
        periods,
        "Август 2026",
        date(2026, 8, 1),
        date(2026, 8, 31)
    )
    assert period.id == 1
    assert period.contains(date(2026, 8, 15))
    assert not period.contains(date(2026, 9, 1))


def test_find_period_by_id() -> None:
    periods: list = []
    create_period(
        periods,
        "Август 2026",
        date(2026, 8, 1),
        date(2026, 8, 31)
    )
    period = find_period_by_id(periods, 1)
    assert period is not None
    assert period.name == "Август 2026"


def test_calculate_period_consumption() -> None:
    objects: list = []
    meters: list = []
    readings: list = []
    periods: list = []
    accounting_object = create_object(objects, "A", "квартира", 20.0)
    meter = create_meter(meters, "ЭЛ-1", "электроэнергия", accounting_object)
    period = create_period(
        periods,
        "Август 2026",
        date(2026, 8, 1),
        date(2026, 8, 31)
    )
    create_reading(readings, meter, 1000.0, date(2026, 8, 1))
    create_reading(readings, meter, 1100.0, date(2026, 8, 20))
    create_reading(readings, meter, 1500.0, date(2026, 9, 5))
    consumption = calculate_period_consumption(
        readings,
        meter.id,
        period
    )
    assert consumption == 100.0
