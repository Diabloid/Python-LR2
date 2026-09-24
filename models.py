# models.py

class Game:
    """Базовий клас для всіх ігор."""
    def __init__(self, title: str, developer: str, year: int, hours_played: list | None = None):
        self._title = title          # Інкапсуляція (захищене поле)
        self._developer = developer
        self.year = year             # Виклик сеттера для валідації
        self._hours_played = hours_played if hours_played is not None else []

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        """Захист від некоректного року випуску."""
        if value < 1950 or value > 2100:
            raise ValueError(f"Некоректний рік випуску: {value}. Рік має бути між 1950 та 2100.")
        self._year = value

    @property
    def title(self):
        return self._title

    def to_dict(self):
        """Серіалізація об'єкта для збереження в JSON."""
        return {
            "type": self.__class__.__name__,
            "title": self._title,
            "developer": self._developer,
            "year": self._year,
            "hours_played": self._hours_played
        }

    def get_gameplay_info(self) -> str:
        return "Стандартна гра без специфічної інформації про геймплей."

    def __str__(self):
        return f"Гра: {self._title} | Розробник: {self._developer} ({self._year})"


class RPGGame(Game):
    """Клас-нащадок для рольових ігор (наприклад, The Witcher 3)."""
    def __init__(self, title: str, developer: str, year: int, missions: int, hours_played: list | None = None):
        super().__init__(title, developer, year, hours_played)
        self._missions = missions

    def to_dict(self):
        data = super().to_dict()
        data["missions"] = self._missions
        return data

    def get_gameplay_info(self) -> str:
        return f"🔥 Жанр: RPG. Має розгалужену кампанію на {self._missions} квестів/місій."

    def __str__(self):
        return super().__str__() + f" | Квестів: {self._missions}"


class ActionGame(Game):
    """Клас-нащадок для екшенів (наприклад, Tomb Raider)."""
    def __init__(self, title: str, developer: str, year: int, is_multiplayer: bool, hours_played: list | None = None):
        super().__init__(title, developer, year, hours_played)
        self._is_multiplayer = is_multiplayer

    def to_dict(self):
        data = super().to_dict()
        data["is_multiplayer"] = self._is_multiplayer
        return data

    def get_gameplay_info(self) -> str:
        mode = "Мультиплеєр доступний" if self._is_multiplayer else "Тільки одиночна гра"
        return f"⚔️ Жанр: Action. Режим гри: {mode}."

    def __str__(self):
        mode = "Multiplayer" if self._is_multiplayer else "Singleplayer"
        return super().__str__() + f" | Режим: {mode}"