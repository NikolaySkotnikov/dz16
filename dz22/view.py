from model import Shoes


def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result
        return wrapper
    return decorator


class View:

    @add_title('Запрос пользователя')
    def get_next_query(self):
        print('1. Посмотреть всю обувь.\n'
              '2. Добавить обувь.\n'
              '3. Удалить обувь.\n'
              '4. Найти обувь.\n'
              '0. Выход\n')
        return input('Введите Ваш запрос: ')

    @add_title('Вся обувь')
    def show_data(self, data):
        if len(data) == 0:
            print('Обуви нет!!!'.center(50, '-'))
        else:
            for key, shoes in enumerate(data, start=1):
                print(f'{key}'.center(50, '-'), f'\n{shoes}')

    @add_title('Введите данные')
    def add_user_shoes(self):
        dict_shoes = {}
        for par in Shoes.shoes_parameters:
            dict_shoes[par] = input(f'Введите {par.lower()}: ')
        return dict_shoes

    @add_title('Поиск обуви')
    def get_keywords(self):
        return input('Введите ключевые слова для поиска обуви: ')

    @add_title('Ничего не найдено')
    def get_massage(self):
        pass

    @add_title('')
    def get_number(self, shoes):
        self.show_data(shoes)
        return int(input('Введите номер обуви, которую хотите удалить: '))
