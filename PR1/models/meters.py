from .objects import AccountingObject


class Meter:
    """Сущность «Счётчик» — прибор учёта на объекте."""

    def __init__(
        self,
        meter_id: int,
        number: str,
        meter_type: str,
        accounting_object: AccountingObject
    ) -> None:
        self.id = meter_id
        self.number = number
        self.meter_type = meter_type
        self.accounting_object = accounting_object
        self.status = "Активен"

    def deactivate(self) -> None:
        """Вывести счётчик из эксплуатации."""
        self.status = "Неактивен"

    def belongs_to(self, object_id: int) -> bool:
        """Проверить, установлен ли счётчик на указанном объекте."""
        return self.accounting_object.id == object_id

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, "
            f"Номер: {self.number}, "
            f"Тип: {self.meter_type}, "
            f"Объект: {self.accounting_object.address}, "
            f"Статус: {self.status}"
        )


def create_meter(
    meters: list[Meter],
    number: str,
    meter_type: str,
    accounting_object: AccountingObject
) -> Meter:
    """Добавить счётчик и привязать его к объекту."""
    meter = Meter(
        len(meters) + 1,
        number,
        meter_type,
        accounting_object
    )
    meters.append(meter)
    return meter


def find_meter_by_id(
    meters: list[Meter],
    meter_id: int
) -> Meter | None:
    """Найти счётчик по идентификатору."""
    for meter in meters:
        if meter.id == meter_id:
            return meter
    return None


def find_meters_by_number(
    meters: list[Meter],
    query: str
) -> list[Meter]:
    """Найти счётчики по подстроке номера."""
    result = []
    for meter in meters:
        if query.lower() in meter.number.lower():
            result.append(meter)
    return result


def filter_meters_by_object(
    meters: list[Meter],
    object_id: int
) -> list[Meter]:
    """Отобрать счётчики выбранного объекта."""
    result = []
    for meter in meters:
        if meter.belongs_to(object_id):
            result.append(meter)
    return result


def show_meters(meters: list[Meter]) -> None:
    """Вывести список счётчиков."""
    if not meters:
        print("Счётчиков нет")
        return
    for meter in meters:
        print(meter)
