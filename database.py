# database.py
import json
from models import Game, RPGGame, ActionGame

class LibraryManager:
    """Клас для управління колекцією ігор та роботи з файлами."""
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.games = []

    def add_game(self, game: Game):
        self.games.append(game)
        print(f"Гру '{game.title}' успішно додано до бібліотеки!")

    def save_to_file(self):
        """Збереження даних у JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([game.to_dict() for game in self.games], f, ensure_ascii=False, indent=4)
        print(f"Бібліотеку збережено у файл '{self.filename}'.")

    def load_from_file(self):
        """Зчитування даних із JSON-файлу з відновленням класів."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.games = []
                for item in data:
                    # Фабрика об'єктів: визначаємо клас за полем 'type'
                    try:
                        if item["type"] == "RPGGame":
                            game = RPGGame(item["title"], item["developer"], item["year"], item["missions"], item["hours_played"])
                        elif item["type"] == "ActionGame":
                            game = ActionGame(item["title"], item["developer"], item["year"], item["is_multiplayer"], item["hours_played"])
                        else:
                            game = Game(item["title"], item["developer"], item["year"], item["hours_played"])
                        self.games.append(game)
                    except ValueError as e:
                        print(f"Помилка завантаження гри '{item.get('title', 'Невідомо')}': {e}")
            print("Дані успішно завантажено з файлу.")
        except FileNotFoundError:
            print("Файл бази даних не знайдено. Створено нову порожню бібліотеку.")
            self.games = []

    def show_all(self):
        if not self.games:
            print("Бібліотека наразі порожня.")
            return

        for index, game in enumerate(self.games):
            print(f"\n[{index}] {game}")
            print(f"    Деталі: {game.get_gameplay_info()}") # Демонстрація поліморфізму