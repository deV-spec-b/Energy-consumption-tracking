def create_object(
    objects: list[dict],
    address: str,
    object_type: str,
    area: float
) -> dict:
    accounting_object = {
        "id": len(objects) + 1,
        "address": address,
        "object_type": object_type,
        "area": area
    }
    objects.append(accounting_object)
    return accounting_object


def find_object_by_id(
    objects: list[dict],
    object_id: int
) -> dict | None:
    for accounting_object in objects:
        if accounting_object["id"] == object_id:
            return accounting_object
    return None


def find_objects_by_address(
    objects: list[dict],
    query: str
) -> list[dict]:
    result = []
    for accounting_object in objects:
        if query.lower() in accounting_object["address"].lower():
            result.append(accounting_object)
    return result


def sort_objects_by_area(objects: list[dict]) -> list[dict]:
    return sorted(objects, key=lambda item: item["area"])


def show_objects(objects: list[dict]) -> None:
    if not objects:
        print("Объектов нет")
        return
    for accounting_object in objects:
        print(
            f"ID: {accounting_object['id']}, "
            f"Адрес: {accounting_object['address']}, "
            f"Тип: {accounting_object['object_type']}, "
            f"Площадь: {accounting_object['area']} м²"
        )
