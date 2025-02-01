import os
from utils import is_directory_valid, show_history


def run_file_browser():
    current_path = os.getcwd()
    while True:
        command = input(f"({current_path}) Podaj polecenie"
                        " (q, ls, cd, pwd, head): ").strip()
        if command == "q":
            break
        elif command == "ls":
            try:
                files = os.listdir(current_path)
                for file in files:
                    print(file)
            except OSError as e:
                print(f"Error: {e}")
        elif command.startswith("cd "):
            new_dir = command[3:].strip()
            if is_directory_valid(new_dir):
                current_path = os.path.abspath(new_dir)
            else:
                print(f"Katalog {new_dir} nie istnieje.")
        elif command == "pwd":
            print(f"Ścieżka bieżąca: {current_path}")
        elif command == "history":
            show_history()
        elif command.startswith("head "):
            file_name = command[5:].strip()
            try:
                with open(file_name, 'rb') as file:
                    print(file.read(512))
            except FileNotFoundError:
                print(f"Plik {file_name} nie istnieje.")
        else:
            print("Nieznane polecenie.")
