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


class Library:
    def __init__(self, books=None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список).
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Следующий идентификатор книги.
        """
        if not self.books:
            return 1
        return max(book.id_ for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по ее идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с запрашиваемым id не существует.
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


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
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1

