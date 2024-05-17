# Задание 2
# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необ-
# ходимую операцию.

class Stack:
    def __init__(self, *args, size):
        self.items = list(args)
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def length(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def peak(self):
        if self.is_empty():
            print('Stack is empty!')
            return
        return self.items[-1]

    def push(self, value):
        if self.is_full():
            print('Stack is full!')
            return
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print('Stack is empty!')
            return
        return self.items.pop()

    def __str__(self):
        result = 'Stack:\n\t'
        result += '\n\t'.join(map(str, reversed(self.items)))
        return result


size_stack = int(input('Введите длину стека: '))

stack = Stack(size=size_stack)

print('1 - помещение строки в стек\n'
      '2 - выталкивание строки из стека\n'
      '3 - подсчет количества строк в стеке\n'
      '4 - проверка пустой ли стек\n'
      '5 - проверка полный ли стек\n'
      '6 - очистка стека\n'
      '7 - получение значения без выталкивания верхней строки\n'
      '8 - показать стек\n'
      '0 - выход\n')

while True:
    command = int(input('Введите команду: '))
    if command == 0:
        print('До свидания!')
        break
    elif command == 1:
        vol = input('Введите строчку для добавления в стек: ')
        stack.push(vol)
    elif command == 2:
        stack.pop()
    elif command == 3:
        print(f'Количество строк стека: {stack.length()}')
    elif command == 4:
        if stack.is_empty():
            print('Стек пустой!')
        else:
            print('Стек не пустой!')
    elif command == 5:
        if stack.is_full():
            print('Стек полный!')
        else:
            print('Стек не полный!')
    elif command == 6:
        stack.clear()
        print('Стек очищен!')
    elif command == 7:
        print(stack.peak())
    elif command == 8:
        print(stack)
