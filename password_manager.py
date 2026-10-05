import getpass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MASTER_FILE = BASE_DIR / "masterpassword.txt"
DATA_FILE = BASE_DIR / "passwords.txt"


def init_files():
    if not MASTER_FILE.exists():
        with open(MASTER_FILE, "w", encoding="utf-8") as f:
            f.write("admin")
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            pass


init_files()

print("\n" * 40)
with open(MASTER_FILE, "r", encoding="utf-8") as file:
    master_password = file.read().strip()

print("Добро пожаловать в терминальный менеджер паролей!")
password = getpass.getpass("Введите Мастер-пароль: ")

if password == master_password:
    print("Доступ разрешен!")
    while True:
        print("\n" * 40)
        print("1 - Добавить пароль")
        print("2 - Посмотреть сохраненный пароль")
        print("3 - Изменить пароль от сайта/сервиса")
        print("4 - Очистить базу паролей")
        print("5 - Выйти")

        choice = input("\nВыберите действие: ")

        if choice == "5":
            break

        elif choice == "1":
            service = input("Введите название сервиса/сайта: ")
            pass_val = input("Введите пароль от сервиса/сайта: ")
            with open(DATA_FILE, "a", encoding="utf-8") as file:
                file.write(f"{service}: {pass_val}\n")
            input("\nПароль успешно сохранен! Нажмите Enter...")

        elif choice == "2":
            search = input("Введите название сайта/сервиса: ").lower()
            found = False
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    if ": " in line:
                        srv, pass_val = line.strip().split(": ", 1)
                        if srv.lower() == search:
                            print(f"\nПароль от {srv}: {pass_val}")
                            found = True
                            break
            if not found:
                print("\nОшибка: такого сайта нет в базе данных!")
            input("\nНажмите Enter чтобы продолжить...")

        elif choice == "3":
            search = input("Пароль от какого сайта хотите изменить?\n").lower()
            new_pass = input("Какой новый пароль хотите установить?\n")
            found = False
            updated_records = []

            with open(DATA_FILE, "r", encoding="utf-8") as file:
                for line in file:
                    if ": " in line:
                        srv, pass_val = line.strip().split(": ", 1)
                        if srv.lower() == search:
                            updated_records.append(f"{srv}: {new_pass}\n")
                            found = True
                        else:
                            updated_records.append(line)

            if found:
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    file.writelines(updated_records)
                print(f"\nПароль успешно изменен для сервиса {search}!")
            else:
                print("\nОшибка: сервис не найден!")
            input("\nНажмите Enter для продолжения...")

        elif choice == "4":
            answer = input(
                "Вы уверены? Все пароли будут удалены! (да/нет): "
            )
            if answer.lower() == "да":
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    pass
                print("\nБаза паролей очищена!")
                input("\nНажмите Enter для продолжения...")
else:
    print("\nОшибка! Неверный мастер-пароль.")