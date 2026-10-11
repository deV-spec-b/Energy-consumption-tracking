def input_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число")


def input_float(prompt: str) -> float:
    """Безопасный ввод вещественного числа."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Введите число")
