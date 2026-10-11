from datetime import date

from .meters import Meter


class Reading:
    """Сущность «Показание» — зафиксированное значение счётчика."""

    def __init__(
        self,
        reading_id: int,
        meter: Meter,
        value: float,
        reading_date: date
    ) -> None:
        self.id = reading_id
        self.meter = meter
        self.value = value
        self.reading_date = reading_date

    def is_later_than(self, other: "Reading") -> bool:
        """Проверить, что показание снято позже другого."""
        return self.reading_date > other.reading_date

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, "
            f"Счётчик: {self.meter.number}, "
            f"Значение: {self.value}, "
            f"Дата: {self.reading_date}"
        )


def create_reading(
    readings: list[Reading],
    meter: Meter,
    value: float,
    reading_date: date
) -> Reading:
    """Добавить показание по счётчику."""
    reading = Reading(
        len(readings) + 1,
        meter,
        value,
        reading_date
    )
    readings.append(reading)
    return reading


def find_reading_by_id(
    readings: list[Reading],
    reading_id: int
) -> Reading | None:
    """Найти показание по идентификатору."""
    for reading in readings:
        if reading.id == reading_id:
            return reading
    return None


def filter_readings_by_meter(
    readings: list[Reading],
    meter_id: int
) -> list[Reading]:
    """Отобрать показания выбранного счётчика."""
    result = []
    for reading in readings:
        if reading.meter.id == meter_id:
            result.append(reading)
    return result


def sort_readings_by_date(
    readings: list[Reading]
) -> list[Reading]:
    """Отсортировать показания по дате."""
    return sorted(readings, key=lambda item: item.reading_date)


def calculate_consumption(
    readings: list[Reading],
    meter_id: int
) -> float | None:
    """Рассчитать расход по счётчику как разницу крайних показаний."""
    meter_readings = sort_readings_by_date(
        filter_readings_by_meter(readings, meter_id)
    )
    if len(meter_readings) < 2:
        return None
    return meter_readings[-1].value - meter_readings[0].value


def show_readings(readings: list[Reading]) -> None:
    """Вывести список показаний."""
    if not readings:
        print("Показаний нет")
        return
    for reading in readings:
        print(reading)
