import json
from datetime import date

from models.meters import Meter
from models.objects import AccountingObject
from models.periods import Period
from models.readings import Reading


def load_json(filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_json(filename: str, data: list) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def load_objects(filename: str) -> list[AccountingObject]:
    data = load_json(filename)
    objects = []
    for item in data:
        objects.append(
            AccountingObject(
                item["id"],
                item["address"],
                item["object_type"],
                item["area"]
            )
        )
    return objects


def save_objects(
    filename: str,
    objects: list[AccountingObject]
) -> None:
    data = []
    for accounting_object in objects:
        data.append({
            "id": accounting_object.id,
            "address": accounting_object.address,
            "object_type": accounting_object.object_type,
            "area": accounting_object.area
        })
    save_json(filename, data)


def load_meters(
    filename: str,
    objects: list[AccountingObject]
) -> list[Meter]:
    data = load_json(filename)
    meters = []
    for item in data:
        accounting_object = None
        for current_object in objects:
            if current_object.id == item["object_id"]:
                accounting_object = current_object
                break
        if accounting_object is None:
            continue
        meter = Meter(
            item["id"],
            item["number"],
            item["meter_type"],
            accounting_object
        )
        meter.status = item.get("status", "Активен")
        meters.append(meter)
    return meters


def save_meters(filename: str, meters: list[Meter]) -> None:
    data = []
    for meter in meters:
        data.append({
            "id": meter.id,
            "number": meter.number,
            "meter_type": meter.meter_type,
            "object_id": meter.accounting_object.id,
            "status": meter.status
        })
    save_json(filename, data)


def load_readings(
    filename: str,
    meters: list[Meter]
) -> list[Reading]:
    data = load_json(filename)
    readings = []
    for item in data:
        meter = None
        for current_meter in meters:
            if current_meter.id == item["meter_id"]:
                meter = current_meter
                break
        if meter is None:
            continue
        year, month, day = item["reading_date"].split("-")
        reading = Reading(
            item["id"],
            meter,
            item["value"],
            date(int(year), int(month), int(day))
        )
        readings.append(reading)
    return readings


def save_readings(filename: str, readings: list[Reading]) -> None:
    data = []
    for reading in readings:
        data.append({
            "id": reading.id,
            "meter_id": reading.meter.id,
            "value": reading.value,
            "reading_date": reading.reading_date.isoformat()
        })
    save_json(filename, data)


def load_periods(filename: str) -> list[Period]:
    data = load_json(filename)
    periods = []
    for item in data:
        start_parts = item["start_date"].split("-")
        end_parts = item["end_date"].split("-")
        periods.append(
            Period(
                item["id"],
                item["name"],
                date(
                    int(start_parts[0]),
                    int(start_parts[1]),
                    int(start_parts[2])
                ),
                date(
                    int(end_parts[0]),
                    int(end_parts[1]),
                    int(end_parts[2])
                )
            )
        )
    return periods


def save_periods(filename: str, periods: list[Period]) -> None:
    data = []
    for period in periods:
        data.append({
            "id": period.id,
            "name": period.name,
            "start_date": period.start_date.isoformat(),
            "end_date": period.end_date.isoformat()
        })
    save_json(filename, data)
