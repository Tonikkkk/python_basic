class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга: {self.name}. Автор: {self.author}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига: {self.name}. Автор: {self.author}. Длительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

# Проверка работы классов
if __name__ == "__main__":
    paper_book = PaperBook("Война и мир", "Л. Толстой", 1225)
    audio_book = AudioBook("1984", "Дж. Оруэлл", 11.5)

    print(paper_book)  # Бумажная книга: Война и мир. Автор: Л. Толстой. Страниц: 1225
    print(audio_book)  # Аудиокнига: 1984. Автор: Дж. Оруэлл. Длительность: 11.5 часов

    print(repr(paper_book))  # PaperBook(name='Война и мир', author='Л. Толстой', pages=1225)
    print(repr(audio_book))  # AudioBook(name='1984', author='Дж. Оруэлл', duration=11.5)

    # Попытка задать некорректные значения
    try:
        paper_book.pages = -100
    except ValueError as e:
        print(e)  # Ошибка: Количество страниц должно быть положительным целым числом.

    try:
        audio_book.duration = -5
    except ValueError as e:
        print(e)  # Ошибка: Продолжительность должна быть положительным числом.