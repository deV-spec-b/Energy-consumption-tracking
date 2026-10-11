from datetime import date

from readings import filter_readings_by_meter, sort_readings_by_date


def create_period(
    periods: list[dict],
    name: str,
    start_date: date,
    end_date: date
) -> dict:
    period = {
        "id": len(periods) + 1,
        "name": name,
        "start_date": start_date,
        "end_date": end_date
    }
    periods.append(period)
    return period


def find_period_by_id(periods: list[dict], period_id: int) -> dict | None:
    for period in periods:
        if period["id"] == period_id:
            return period
    return None


def period_contains(period: dict, check_date: date) -> bool:
    return period["start_date"] <= check_date <= period["end_date"]


def calculate_period_consumption(
    readings: list[dict],
    meter_id: int,
    period: dict
) -> float | None:
    period_readings = []
    for reading in filter_readings_by_meter(readings, meter_id):
        if period_contains(period, reading["reading_date"]):
            period_readings.append(reading)
    period_readings = sort_readings_by_date(period_readings)
    if len(period_readings) < 2:
        return None
    return period_readings[-1]["value"] - period_readings[0]["value"]


def show_periods(periods: list[dict]) -> None:
    if not periods:
        print("Периодов нет")
        return
    for period in periods:
        print(
            f"ID: {period['id']}, "
            f"Название: {period['name']}, "
            f"С: {period['start_date']}, "
            f"По: {period['end_date']}"
        )
