class AccountingObject:
    """Сущность «Объект» — квартира, помещение или здание учёта."""

    def __init__(
        self,
        object_id: int,
        address: str,
        object_type: str,
        area: float
    ) -> None:
        self.id = object_id
        self.address = address
        self.object_type = object_type
        self.area = area

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, "
            f"Адрес: {self.address}, "
            f"Тип: {self.object_type}, "
            f"Площадь: {self.area} м²"
        )


def create_object(
    objects: list[AccountingObject],
    address: str,
    object_type: str,
    area: float
) -> AccountingObject:
    """Добавить объект учёта."""
    accounting_object = AccountingObject(
        len(objects) + 1,
        address,
        object_type,
        area
    )
    objects.append(accounting_object)
    return accounting_object


def find_object_by_id(
    objects: list[AccountingObject],
    object_id: int
) -> AccountingObject | None:
    """Найти объект по идентификатору."""
    for accounting_object in objects:
        if accounting_object.id == object_id:
            return accounting_object
    return None


def find_objects_by_address(
    objects: list[AccountingObject],
    query: str
) -> list[AccountingObject]:
    """Найти объекты по подстроке адреса."""
    result = []
    for accounting_object in objects:
        if query.lower() in accounting_object.address.lower():
            result.append(accounting_object)
    return result


def filter_objects_by_type(
    objects: list[AccountingObject],
    object_type: str
) -> list[AccountingObject]:
    """Отобрать объекты по типу."""
    result = []
    for accounting_object in objects:
        if accounting_object.object_type.lower() == object_type.lower():
            result.append(accounting_object)
    return result


def sort_objects_by_area(
    objects: list[AccountingObject]
) -> list[AccountingObject]:
    """Отсортировать объекты по площади."""
    return sorted(objects, key=lambda item: item.area)


def show_objects(objects: list[AccountingObject]) -> None:
    """Вывести список объектов."""
    if not objects:
        print("Объектов нет")
        return
    for accounting_object in objects:
        print(accounting_object)
