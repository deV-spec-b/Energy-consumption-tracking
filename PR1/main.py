from datetime import date


object_address = "ул. Ленина, д. 10, кв. 15"
meter_number = "ЭЛ-1001"
previous_value = 1200.0
new_value = 1285.5
reading_date = date(2026, 9, 1)


def is_reading_valid(previous_value, new_value):
    if new_value >= previous_value:
        return True
    return False


def calculate_consumption(previous_value, new_value):
    return new_value - previous_value


def get_accounting_status(object_address, meter_number, consumption):
    return (
        f"Объект: {object_address}; "
        f"Счётчик: {meter_number}; "
        f"Расход: {consumption}"
    )


print(f"Дата: {reading_date}")
print(f"Объект: {object_address}")
print(f"Счётчик: {meter_number}")
print(f"Предыдущее показание: {previous_value}")
print(f"Новое показание: {new_value}")

if is_reading_valid(previous_value, new_value):
    consumption = calculate_consumption(previous_value, new_value)
    print(get_accounting_status(object_address, meter_number, consumption))
else:
    print("Показание меньше предыдущего, данные не приняты")
