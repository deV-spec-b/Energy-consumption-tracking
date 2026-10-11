from datetime import date

from readings import calculate_consumption, create_reading


def test_calculate_consumption() -> None:
    readings: list = []
    create_reading(readings, 1, 1200.0, date(2026, 8, 1))
    create_reading(readings, 1, 1285.5, date(2026, 9, 1))
    assert calculate_consumption(readings, 1) == 85.5
