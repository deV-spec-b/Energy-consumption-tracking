from datetime import date

from .readings import Reading, filter_readings_by_meter, sort_readings_by_date


class Period:
    """Сущность «Период» — интервал, за который считается потребление."""

    def __init__(
        self,
        period_id: int,
        name: str,
        start_date: date,
        end_date: date
    ) -> None:
        self.id = period_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def contains(self, check_date: date) -> bool:
        """Проверить, входит ли дата в период."""
        return self.start_date <= check_date <= self.end_date

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, "
            f"Название: {self.name}, "
            f"С: {self.start_date}, "
            f"По: {self.end_date}"
        )


def create_period(
    periods: list[Period],
    name: str,
    start_date: date,
    end_date: date
) -> Period:
    """Добавить период учёта."""
    period = Period(
        len(periods) + 1,
        name,
        start_date,
        end_date
    )
    periods.append(period)
    return period


def find_period_by_id(
    periods: list[Period],
    period_id: int
) -> Period | None:
    """Найти период по идентификатору."""
    for period in periods:
        if period.id == period_id:
            return period
    return None


def filter_readings_by_period(
    readings: list[Reading],
    period: Period
) -> list[Reading]:
    """Отобрать показания, снятые в выбранном периоде."""
    result = []
    for reading in readings:
        if period.contains(reading.reading_date):
            result.append(reading)
    return result


def calculate_period_consumption(
    readings: list[Reading],
    meter_id: int,
    period: Period
) -> float | None:
    """Рассчитать расход счётчика за период."""
    period_readings = sort_readings_by_date(
        filter_readings_by_meter(
            filter_readings_by_period(readings, period),
            meter_id
        )
    )
    if len(period_readings) < 2:
        return None
    return period_readings[-1].value - period_readings[0].value


def show_periods(periods: list[Period]) -> None:
    """Вывести список периодов."""
    if not periods:
        print("Периодов нет")
        return
    for period in periods:
        print(period)
