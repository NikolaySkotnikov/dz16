# 1. Создайте функцию, возвращающую список со всеми
# простыми числами от 0 до 1000.
# Используя механизм декораторов посчитайте сколько
# секунд, потребовалось для вычисления всех простых чисел.
# Отобразите на экран количество секунд и простые числа.
import time


def timer(fun):
    def wrapper(*args):
        start = time.time()
        result = fun(*args)
        print(f'Время выполнения:  {time.time() - start} секунд.')
        return result
    return wrapper


@timer
def simple_number():
    numbers = []
    for num in range(0, 1001):
        k = 0
        for i in range(1, num + 1):
            if num <= 1:
                break
            if num % i == 0:
                k += 1
        if k == 2:
            numbers.append(num)
    return print(f'Простые числа от 0 до 1000: {numbers}')


simple_number()


# 2. Добавьте к первому заданию возможность передавать
# границы диапазона для поиска всех простых чисел.

@timer
def simple_number2(start: int, end: int) -> list:
    numbers = []
    for num in range(start, end + 1):
        k = 0
        for i in range(1, num + 1):
            if num <= 1:
                break
            if num % i == 0:
                k += 1
        if k == 2:
            numbers.append(num)
    return numbers


print(simple_number2(-10, 1680))

# 3. Реализуйте декоратор для обработки исключений,
# возникающих внутри функции, и вывода
# соответствующего сообщения об ошибке.


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(f'Ошибка: {err}')
            return None
    return wrapper


@exception_handler
def divide(n):
    return 1 / n


print(divide(1))
print(divide(0))
print(divide(3))


# 4. Создайте декоратор, который применяется к классу и
# изменяет его поведение или добавляет новые методы.


def add_prefix(prefix):
    def class_decorator(cls):
        class DecoratedClass(cls):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.prefix = prefix

            def get_prefixed_name(self):
                return self.prefix + self.name
        return DecoratedClass
    return class_decorator


@add_prefix("Mr. ")
class Person:
    def __init__(self, name):
        self.name = name


person1 = Person("John")
person2 = Person("Lewis")
print(person1.get_prefixed_name())
print(person2.get_prefixed_name())
