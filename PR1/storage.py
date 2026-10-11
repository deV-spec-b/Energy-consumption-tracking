import json
from datetime import date


def load_json(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_json(filename: str, data: list) -> None:
    ready = []
    for item in data:
        row = dict(item)
        for key, value in row.items():
            if isinstance(value, date):
                row[key] = value.isoformat()
        ready.append(row)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(ready, file, ensure_ascii=False, indent=4)


def parse_iso_date(value: str) -> date:
    year, month, day = value.split("-")
    return date(int(year), int(month), int(day))


def load_objects(filename: str) -> list[dict]:
    return load_json(filename)


def save_objects(filename: str, objects: list[dict]) -> None:
    save_json(filename, objects)


def load_meters(filename: str) -> list[dict]:
    return load_json(filename)


def save_meters(filename: str, meters: list[dict]) -> None:
    save_json(filename, meters)


def load_readings(filename: str) -> list[dict]:
    readings = load_json(filename)
    for reading in readings:
        reading["reading_date"] = parse_iso_date(reading["reading_date"])
    return readings


def save_readings(filename: str, readings: list[dict]) -> None:
    save_json(filename, readings)


def load_periods(filename: str) -> list[dict]:
    periods = load_json(filename)
    for period in periods:
        period["start_date"] = parse_iso_date(period["start_date"])
        period["end_date"] = parse_iso_date(period["end_date"])
    return periods


def save_periods(filename: str, periods: list[dict]) -> None:
    save_json(filename, periods)
