from calculator import run_calculator
from file_handling import run_file_browser
from utils import clear_history


def main():
    while True:
        command = input("Podaj polecenie (quit, calc, files): ").strip()
        if command == "quit":
            clear_history("history.txt")
            print("Kończę program...")
            exit(0)
        elif command == "calc":
            run_calculator()
        elif command == "files":
            run_file_browser()
        else:
            print("Nieznane polecenie.")


if __name__ == "__main__":
    clear_history("history.txt")
    main()
