from datetime import date

from models.meters import (
    create_meter,
    find_meter_by_id,
    find_meters_by_number,
    filter_meters_by_object,
    show_meters
)
from models.objects import (
    create_object,
    find_object_by_id,
    find_objects_by_address,
    show_objects,
    sort_objects_by_area
)
from models.periods import (
    calculate_period_consumption,
    create_period,
    find_period_by_id,
    show_periods
)
from models.readings import (
    calculate_consumption,
    create_reading,
    show_readings
)
from storage import (
    load_meters,
    load_objects,
    load_periods,
    load_readings,
    save_meters,
    save_objects,
    save_periods,
    save_readings
)
from utils import input_float, input_int


OBJECTS_FILE = "data/objects.json"
METERS_FILE = "data/meters.json"
READINGS_FILE = "data/readings.json"
PERIODS_FILE = "data/periods.json"


def parse_date(prompt: str) -> date:
    raw_value = input(prompt)
    year, month, day = raw_value.split("-")
    return date(int(year), int(month), int(day))


def save_all(objects, meters, readings, periods) -> None:
    save_objects(OBJECTS_FILE, objects)
    save_meters(METERS_FILE, meters)
    save_readings(READINGS_FILE, readings)
    save_periods(PERIODS_FILE, periods)


def main() -> None:
    objects = load_objects(OBJECTS_FILE)
    meters = load_meters(METERS_FILE, objects)
    readings = load_readings(READINGS_FILE, meters)
    periods = load_periods(PERIODS_FILE)

    while True:
        print("\n=== Учёт энергопотребления ===\n")
        print("1. Показать объекты")
        print("2. Добавить объект")
        print("3. Найти объект по адресу")
        print("4. Показать объекты по площади")
        print("5. Показать счётчики")
        print("6. Добавить счётчик")
        print("7. Найти счётчик по номеру")
        print("8. Счётчики объекта")
        print("9. Показать показания")
        print("10. Внести показание")
        print("11. Рассчитать расход по счётчику")
        print("12. Показать периоды")
        print("13. Добавить период")
        print("14. Рассчитать расход за период")
        print("0. Выход")

        choice = input_int("Выберите действие: ")

        if choice == 1:
            show_objects(objects)

        elif choice == 2:
            address = input("Адрес объекта: ")
            object_type = input("Тип объекта: ")
            area = input_float("Площадь: ")
            create_object(objects, address, object_type, area)
            save_objects(OBJECTS_FILE, objects)
            print("Объект добавлен")

        elif choice == 3:
            query = input("Подстрока адреса: ")
            found = find_objects_by_address(objects, query)
            show_objects(found)

        elif choice == 4:
            show_objects(sort_objects_by_area(objects))

        elif choice == 5:
            show_meters(meters)

        elif choice == 6:
            number = input("Номер счётчика: ")
            meter_type = input("Тип счётчика: ")
            object_id = input_int("ID объекта: ")
            accounting_object = find_object_by_id(objects, object_id)
            if accounting_object is None:
                print("Объект не найден")
                continue
            create_meter(meters, number, meter_type, accounting_object)
            save_meters(METERS_FILE, meters)
            print("Счётчик добавлен")

        elif choice == 7:
            query = input("Подстрока номера: ")
            found = find_meters_by_number(meters, query)
            show_meters(found)

        elif choice == 8:
            object_id = input_int("ID объекта: ")
            found = filter_meters_by_object(meters, object_id)
            show_meters(found)

        elif choice == 9:
            show_readings(readings)

        elif choice == 10:
            meter_id = input_int("ID счётчика: ")
            meter = find_meter_by_id(meters, meter_id)
            if meter is None:
                print("Счётчик не найден")
                continue
            value = input_float("Значение показания: ")
            try:
                reading_date = parse_date("Дата (ГГГГ-ММ-ДД): ")
            except ValueError:
                print("Некорректная дата")
                continue
            create_reading(readings, meter, value, reading_date)
            save_readings(READINGS_FILE, readings)
            print("Показание внесено")

        elif choice == 11:
            meter_id = input_int("ID счётчика: ")
            consumption = calculate_consumption(readings, meter_id)
            if consumption is None:
                print("Недостаточно показаний для расчёта")
            else:
                print("Расход:", consumption)

        elif choice == 12:
            show_periods(periods)

        elif choice == 13:
            name = input("Название периода: ")
            try:
                start_date = parse_date("Дата начала (ГГГГ-ММ-ДД): ")
                end_date = parse_date("Дата окончания (ГГГГ-ММ-ДД): ")
            except ValueError:
                print("Некорректная дата")
                continue
            if start_date > end_date:
                print("Дата начала позже даты окончания")
                continue
            create_period(periods, name, start_date, end_date)
            save_periods(PERIODS_FILE, periods)
            print("Период добавлен")

        elif choice == 14:
            meter_id = input_int("ID счётчика: ")
            period_id = input_int("ID периода: ")
            period = find_period_by_id(periods, period_id)
            if period is None:
                print("Период не найден")
                continue
            consumption = calculate_period_consumption(
                readings,
                meter_id,
                period
            )
            if consumption is None:
                print("Недостаточно показаний за период")
            else:
                print("Расход за период:", consumption)

        elif choice == 0:
            save_all(objects, meters, readings, periods)
            print("Программа завершена")
            break

        else:
            print("Такого пункта нет")


if __name__ == "__main__":
    main()
