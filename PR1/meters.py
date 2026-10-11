def create_meter(
    meters: list[dict],
    number: str,
    meter_type: str,
    object_id: int
) -> dict:
    meter = {
        "id": len(meters) + 1,
        "number": number,
        "meter_type": meter_type,
        "object_id": object_id,
        "status": "Активен"
    }
    meters.append(meter)
    return meter


def find_meter_by_id(meters: list[dict], meter_id: int) -> dict | None:
    for meter in meters:
        if meter["id"] == meter_id:
            return meter
    return None


def filter_meters_by_object(
    meters: list[dict],
    object_id: int
) -> list[dict]:
    result = []
    for meter in meters:
        if meter["object_id"] == object_id:
            result.append(meter)
    return result


def show_meters(meters: list[dict]) -> None:
    if not meters:
        print("Счётчиков нет")
        return
    for meter in meters:
        print(
            f"ID: {meter['id']}, "
            f"Номер: {meter['number']}, "
            f"Тип: {meter['meter_type']}, "
            f"Объект ID: {meter['object_id']}, "
            f"Статус: {meter['status']}"
        )
