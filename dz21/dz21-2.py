# Задание 2.
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл. При реализации
# используйте паттерн Proxy (для логирования)
# и другие необходимые паттерны.


class ListNumbers:
    def __init__(self, filename):
        self.filename = filename
        self.add_data()
        self.__data = self.load_data()
        self.logger = ProxyLogger('log.txt')

    def add_data(self):
        with open(self.filename, 'w') as file:
            file.write(input('Введите числа через пробел: '))

    def load_data(self):
        with open(self.filename, 'r') as file:
            data = list(map(int, file.read().split()))
        return data

    @property
    def data(self):
        self.logger.log()
        return self.__data

    def get_sum(self):
        return sum(self.data)

    def get_min(self):
        return min(self.data)

    def get_max(self):
        return max(self.data)

    def list_numbers(self):
        return self.data


class ProxyLogger:
    def __init__(self, filename):
        self.filename = filename

    def log(self):
        import datetime
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f'Доступ к файлу с числами {datetime.datetime.now().time()}.\n')


f = ListNumbers('nums.txt')
print(f.list_numbers())
print(f.get_sum())
print(f.get_min())
print(f.get_max())
