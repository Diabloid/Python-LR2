# main.py
from database import LibraryManager
from models import RPGGame, ActionGame
from utils import get_int, get_bool

def main():
    manager = LibraryManager()
    manager.load_from_file() # Спроба завантажити існуючі дані при старті

    while True:
        print("\n=== ООП STEAM LIBRARY MANAGER ===")
        print("1. Додати RPG гру (The Witcher, Mass Effect тощо)")
        print("2. Додати Action гру (Tomb Raider, Cyberpunk тощо)")
        print("3. Показати бібліотеку")
        print("4. Зберегти у файл")
        print("0. Вийти")
        
        choice = input("Оберіть дію: ")
        
        if choice == '1':
            print("\n-- Додавання RPG --")
            title = input("Назва: ")
            dev = input("Розробник: ")
            year = get_int("Рік випуску: ")
            missions = get_int("Кількість квестів: ")
            try:
                game = RPGGame(title, dev, year, missions)
                manager.add_game(game)
            except ValueError as e:
                print(f"Помилка створення об'єкта: {e}")

        elif choice == '2':
            print("\n-- Додавання Action --")
            title = input("Назва: ")
            dev = input("Розробник: ")
            year = get_int("Рік випуску: ")
            is_multi = get_bool("Є мультиплеєр? (так/ні): ")
            try:
                game = ActionGame(title, dev, year, is_multi)
                manager.add_game(game)
            except ValueError as e:
                print(f"Помилка створення об'єкта: {e}")

        elif choice == '3':
            print("\n-- Ваша бібліотека --")
            manager.show_all()

        elif choice == '4':
            manager.save_to_file()

        elif choice == '0':
            # Зберігаємо автоматично перед виходом
            manager.save_to_file()
            print("Вихід з програми. Дані збережено. До зустрічі!")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()