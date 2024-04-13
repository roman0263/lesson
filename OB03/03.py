class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Сохранение автора в атрибуте класса

    def get_info_book(self):
        print(f"{self.title} - {self.author.name}")  # Исправление кавычек и доступ к имени автора

# Создание объекта автора
author = Author("Лев Толстой", "Русский")
# Создание объекта книги
book = Book("Война и мир", author)

# Вызов метода для вывода информации о книге
book.get_info_book()
print(author.name)
