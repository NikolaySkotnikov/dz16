# Задание 1.
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.
# Задание 2.
# Создайте приложение для приготовления пасты. Приложение
# должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

from abc import ABC, abstractmethod


class TypeOfPaste:
    long_paste = 'длинная паста'
    medium_paste = 'средняя паста'
    short_pasta = 'короткая паста'


class Sauce:
    pesto = 'песто'
    tomato = 'томатный'
    creamy = 'сливочный'


class Filling:
    chicken = 'курица'
    ground_meat = 'фарш'
    seafood = 'морепродукты'


class Supplements:
    bacon = 'бекон'
    chess = 'сыр'
    greenery = 'зелень'


class Paste:
    def __init__(self, name):
        self.name = name
        self.type_of_paste = None
        self.sauce = None
        self.filling = None
        self.supplements = []

    def __str__(self):
        if len(self.supplements) > 0:
            result = ''
            for i in self.supplements:
                result += i + ', '
            info = (f'Название: {self.name}\n'
                    f'Тип пасты: {self.type_of_paste}\n'
                    f'Соус: {self.sauce}\n'
                    f'Начинка: {self.filling}\n'
                    f'Добавки: {result[:len(result) - 2]}\n')
        else:
            info = (f'Название: {self.name}\n'
                    f'Тип пасты: {self.type_of_paste}\n'
                    f'Соус: {self.sauce}\n'
                    f'Начинка: {self.filling}\n')
        return info


class BuilderPaste(ABC):
    @abstractmethod
    def choose_type_of_paste(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass

    @abstractmethod
    def add_supplements(self):
        pass


class CarbonaraBuilder(BuilderPaste):
    def __init__(self):
        self.product = Paste('Карбонара')

    def choose_type_of_paste(self):
        self.product.type_of_paste = TypeOfPaste().long_paste

    def add_sauce(self):
        self.product.sauce = Sauce().tomato

    def add_filling(self):
        self.product.filling = Filling().chicken

    def add_supplements(self):
        self.product.supplements.append(Supplements.bacon)
        self.product.supplements.append(Supplements.chess)

    def get_product(self):
        return self.product


class PestoBuilder(BuilderPaste):
    def __init__(self):
        self.product = Paste('Песто')

    def choose_type_of_paste(self):
        self.product.type_of_paste = TypeOfPaste().medium_paste

    def add_sauce(self):
        self.product.sauce = Sauce().pesto

    def add_filling(self):
        self.product.filling = Filling().ground_meat

    def add_supplements(self):
        pass

    def get_product(self):
        return self.product


class PastaWithSeafoodBuilder(BuilderPaste):
    def __init__(self):
        self.product = Paste('Морская')

    def choose_type_of_paste(self):
        self.product.type_of_paste = TypeOfPaste().short_pasta

    def add_sauce(self):
        self.product.sauce = Sauce().creamy

    def add_filling(self):
        self.product.filling = Filling().seafood

    def add_supplements(self):
        self.product.supplements.append(Supplements().greenery)

    def get_product(self):
        return self.product


class Director:
    def make_paste(self, builder):
        builder.choose_type_of_paste()
        builder.add_sauce()
        builder.add_filling()
        builder.add_supplements()
        return builder.get_product()


director = Director()
builder1 = CarbonaraBuilder()
builder2 = PestoBuilder()
builder3 = PastaWithSeafoodBuilder()
print(director.make_paste(builder1))
print(director.make_paste(builder2))
print(director.make_paste(builder3))

# Задание 3.
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

import copy


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Person(Prototype):
    def __init__(self, name: str, address: object):
        self.name = name
        self.address = copy.deepcopy(address)

    def clone(self):
        obj = Person(self.name, self.address)

        return obj

    def __str__(self):
        return f'Имя: {self.name}, адрес: {self.address}'


class Address:
    def __init__(self, number: int, street: str, country: str):
        self.number = number
        self. street = street
        self.country = country

    def __str__(self):
        return f'дом - {self.number}, улица - {self.street}, страна - {self.country}'


ad = Address(35, 'Lenina', 'Russia')
p1 = Person('John', ad)
print(p1)
p2 = p1.clone()
print(p2)
print('------------')
p2.name = 'Jane'
p2.address.number = 45
p2.address.street = 'Leningradskaya'
print(p1)
print(p2)
