# Создайте приложение для работы в библиотеке. Оно
# должно оперировать следующими сущностями: Книга,
# Библиотекарь, Читатель. Приложение должно позволять
# вводить, удалять, изменять, сохранять в файл, загружать из
# файла, логгировать действия, искать информацию (результаты
# поиска выводятся на экран или файл) о сущностях.
# При реализации используйте максимально возможное
# количество паттернов проектирования.

from abc import ABC, abstractmethod


def add_log(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import datetime
            with open('log.txt', 'a', encoding='utf-8') as file:
                file.write(f'{title} {datetime.datetime.now()} {args[1].title}\n')
            result = func(*args, **kwargs)
            print(f'{title} {datetime.datetime.now()} {args[1].title}\n')
            return result
        return wrapper
    return decorator


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class LibrarianOrReader:
    def __init__(self):
        self.filename = None

    @abstractmethod
    def add_book(self, book):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'{book.title}, {book.author}\n')

    @abstractmethod
    def remove_book(self, book):
        result = []
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                result.append(line.strip().split(', '))
        if [book.title, book.author] in result:
            result.remove([book.title, book.author])
            with open(self.filename, 'w', encoding='utf-8') as file:
                for book in result:
                    file.write(f"{', '.join(book)}\n")


class Librarian(LibrarianOrReader):
    def __init__(self, name, filename):
        super().__init__()
        self.name = name
        self.filename = filename
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write('Книги в библиотеке:\n')

    @add_log('Книга добавлена в библиотеку.')
    def add_book(self, book):
        super().add_book(book)

    @add_log('Книга взята из библиотеки')
    def remove_book(self, book):
        super().remove_book(book)


class Reader(LibrarianOrReader):
    def __init__(self, name, filename):
        super().__init__()
        self.name = name
        self.filename = filename
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(f'Книги у читателя {self.name}:\n')

    @add_log('Книгу взял читатель.')
    def add_book(self, book):
        super().add_book(book)

    @add_log('Книгу вернул читатель.')
    def remove_book(self, book):
        super().remove_book(book)


class Director:
    @staticmethod
    def book_to_reader(book, librarian, reader):
        librarian.remove_book(book)
        reader.add_book(book)

    @staticmethod
    def book_to_librarian(book, librarian, reader):
        librarian.add_book(book)
        reader.remove_book(book)


b1 = Book('Book1', 'Author1')
b2 = Book('Book2', 'Author2')
b3 = Book('Book3', 'Author3')
b4 = Book('Book4', 'Author4')
b5 = Book('Book5', 'Author5')

l1 = Librarian('Librian1', 'lib1.txt')
r1 = Reader('Reader1', 'reader1.txt')

l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
l1.add_book(b4)
l1.add_book(b5)

d1 = Director()

d1.book_to_reader(b1, l1, r1)
d1.book_to_reader(b2, l1, r1)
d1.book_to_librarian(b2, l1, r1)
