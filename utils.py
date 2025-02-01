import os


def convert_to_number(input_string):
    try:
        return float(input_string)
    except ValueError:
        return None


def is_directory_valid(directory):
    return os.path.isdir(directory)


def log_history(file_name, operation, num1, num2, result):
    with open(file_name, "a") as f:
        f.write(f"{num1} {operation} {num2} = {result}\n")


def clear_history(file_name):
    try:
        if os.path.exists(file_name):
            with open(file_name, 'w') as file:
                file.truncate(0)
            print(f"Plik '{file_name}' został pomyślnie wyczyszczony.")
        else:
            print(f"Plik '{file_name}' nie został znaleziony.")
            with open("history.txt", "w"):
                pass
    except Exception as e:
        print(f"Błąd podczas czyszczenia pliku: {e}")


def show_history():
    try:
        with open("history.txt", "r") as history_file:
            history = history_file.readlines()
            if history:
                print("Historia działań:")
                for line in history:
                    print(line.strip())
            else:
                print("Brak historii.")
    except FileNotFoundError:
        print("Brak pliku historii.")
