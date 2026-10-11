from datetime import date


def create_reading(
    readings: list[dict],
    meter_id: int,
    value: float,
    reading_date: date
) -> dict:
    reading = {
        "id": len(readings) + 1,
        "meter_id": meter_id,
        "value": value,
        "reading_date": reading_date
    }
    readings.append(reading)
    return reading


def filter_readings_by_meter(
    readings: list[dict],
    meter_id: int
) -> list[dict]:
    result = []
    for reading in readings:
        if reading["meter_id"] == meter_id:
            result.append(reading)
    return result


def sort_readings_by_date(readings: list[dict]) -> list[dict]:
    return sorted(readings, key=lambda item: item["reading_date"])


def calculate_consumption(
    readings: list[dict],
    meter_id: int
) -> float | None:
    meter_readings = sort_readings_by_date(
        filter_readings_by_meter(readings, meter_id)
    )
    if len(meter_readings) < 2:
        return None
    return meter_readings[-1]["value"] - meter_readings[0]["value"]


def show_readings(readings: list[dict]) -> None:
    if not readings:
        print("Показаний нет")
        return
    for reading in readings:
        print(
            f"ID: {reading['id']}, "
            f"Счётчик ID: {reading['meter_id']}, "
            f"Значение: {reading['value']}, "
            f"Дата: {reading['reading_date']}"
        )
