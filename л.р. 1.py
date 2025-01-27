class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        :param id_: Идентификатор книги (должен быть положительным целым числом).
        :param name: Название книги (не должно быть пустой строкой).
        :param pages: Количество страниц в книге (должно быть положительным целым числом).

        :raises ValueError: Если id_ или pages не положительные числа, или если name пустая строка.
        """
        if id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        if not name:
            raise ValueError("Название книги не должно быть пустым.")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает валидную строку Python для создания такого же экземпляра."""
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # Инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # Проверяем метод __str__

    print(list_books)  # Проверяем метод __repr__

