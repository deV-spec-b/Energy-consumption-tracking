from datetime import date

from meters import (
    create_meter,
    filter_meters_by_object,
    find_meter_by_id,
    show_meters
)
from objects import (
    create_object,
    find_object_by_id,
    find_objects_by_address,
    show_objects,
    sort_objects_by_area
)
from periods import (
    calculate_period_consumption,
    create_period,
    find_period_by_id,
    show_periods
)
from readings import (
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


def main() -> None:
    objects = load_objects(OBJECTS_FILE)
    meters = load_meters(METERS_FILE)
    readings = load_readings(READINGS_FILE)
    periods = load_periods(PERIODS_FILE)

    while True:
        print("\n=== Учёт энергопотребления ===\n")
        print("1. Показать объекты")
        print("2. Добавить объект")
        print("3. Найти объект по адресу")
        print("4. Показать объекты по площади")
        print("5. Показать счётчики")
        print("6. Добавить счётчик")
        print("7. Счётчики объекта")
        print("8. Показать показания")
        print("9. Внести показание")
        print("10. Рассчитать расход по счётчику")
        print("11. Показать периоды")
        print("12. Добавить период")
        print("13. Рассчитать расход за период")
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
            show_objects(find_objects_by_address(objects, query))
        elif choice == 4:
            show_objects(sort_objects_by_area(objects))
        elif choice == 5:
            show_meters(meters)
        elif choice == 6:
            number = input("Номер счётчика: ")
            meter_type = input("Тип счётчика: ")
            object_id = input_int("ID объекта: ")
            if find_object_by_id(objects, object_id) is None:
                print("Объект не найден")
                continue
            create_meter(meters, number, meter_type, object_id)
            save_meters(METERS_FILE, meters)
            print("Счётчик добавлен")
        elif choice == 7:
            object_id = input_int("ID объекта: ")
            show_meters(filter_meters_by_object(meters, object_id))
        elif choice == 8:
            show_readings(readings)
        elif choice == 9:
            meter_id = input_int("ID счётчика: ")
            if find_meter_by_id(meters, meter_id) is None:
                print("Счётчик не найден")
                continue
            value = input_float("Значение показания: ")
            try:
                reading_date = parse_date("Дата (ГГГГ-ММ-ДД): ")
            except ValueError:
                print("Некорректная дата")
                continue
            create_reading(readings, meter_id, value, reading_date)
            save_readings(READINGS_FILE, readings)
            print("Показание внесено")
        elif choice == 10:
            meter_id = input_int("ID счётчика: ")
            consumption = calculate_consumption(readings, meter_id)
            if consumption is None:
                print("Недостаточно показаний для расчёта")
            else:
                print("Расход:", consumption)
        elif choice == 11:
            show_periods(periods)
        elif choice == 12:
            name = input("Название периода: ")
            try:
                start_date = parse_date("Дата начала (ГГГГ-ММ-ДД): ")
                end_date = parse_date("Дата окончания (ГГГГ-ММ-ДД): ")
            except ValueError:
                print("Некорректная дата")
                continue
            create_period(periods, name, start_date, end_date)
            save_periods(PERIODS_FILE, periods)
            print("Период добавлен")
        elif choice == 13:
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
            save_objects(OBJECTS_FILE, objects)
            save_meters(METERS_FILE, meters)
            save_readings(READINGS_FILE, readings)
            save_periods(PERIODS_FILE, periods)
            print("Программа завершена")
            break
        else:
            print("Такого пункта нет")


if __name__ == "__main__":
    main()
