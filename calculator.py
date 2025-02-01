import math
from utils import convert_to_number, log_history


def run_calculator():
    history_file = "history.txt"
    while True:
        operation = input("Podaj operację (+, -, *, /, !, ^)"
                          " lub 'q' aby wyjść: ").strip()
        if operation == "q":
            break

        if operation in ['+', '-', '*', '/', '^']:
            num1 = input("Podaj pierwszą liczbę: ")
            num2 = input("Podaj drugą liczbę: ")

            num1 = convert_to_number(num1)
            num2 = convert_to_number(num2)

            if num1 is None or num2 is None:
                print("Wprowadzone wartości muszą być liczbami!")
                continue

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Nie można dzielić przez zero!")
                    continue
                result = num1 / num2
            elif operation == '^':
                result = num1 ** num2
            print(f"Wynik: {result}")
            log_history(history_file, operation, num1, num2, result)

        elif operation == '!':
            num = input("Podaj liczbę do obliczenia silni: ")
            num = convert_to_number(num)
            if num is None or not num.is_integer() or num < 0:
                print("Silnia jest zdefiniowana tylko dla\
                     liczb całkowitych nieujemnych.")
                continue
            result = math.factorial(int(num))
            print(f"Wynik silni: {result}")
            log_history(history_file, "!", num, "-", result)
        else:
            print("Nieznana operacja.")
