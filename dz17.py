# Задание 1
# Пользователь вводит с клавиатуры набор чисел. По-
# лученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число су-
# ществует в списке, нужно вывести сообщение поль-
# зователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления)
# 3. Показать содержимое списка (в зависимости от вы-
# бора пользователя список нужно показать с начала
# или с конца)
# 4. Проверить есть ли значение в списке
# 5. Заменить значение в списке (пользователь опреде-
# ляет заменить ли только первое вхождение или все
# вхождения)
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова.


class SingleList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def append(self, element):
        node = self.Node(element)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = node

    def append_new_num(self, element):
        node = self.Node(element)
        if self.head is None:
            self.head = node
            return
        current = self.head
        if current.value == element:
            print('Такое число существует в списке!!!')
            return
        count = 0
        while current.next_node:
            if current.value == element:
                current = current.next_node
                count += 1
            else:
                current = current.next_node
        if count > 0:
            print('Такое число существует в списке!!!')
            return
        current.next_node = node

    def delite_all_element(self, element):
        if self.head is None:
            print('Список пустой!')
            return
        while self.head.value == element:
            if self.head.next_node:
                self.head = self.head.next_node
            else:
                self.head = None
                return
        current = self.head
        while current.next_node:
            if current.next_node.value == element:
                if current.next_node.next_node:
                    current.next_node = current.next_node.next_node
                    continue
                else:
                    current.next_node = None
                    return
            current = current.next_node

    def contains(self, element):
        if self.head is None:
            print('Список пустой!')
            return False
        current = self.head
        while current:
            if current.value == element:
                print(f'В списке есть число {element}!')
                return True
            current = current.next_node
        print(f'В списке нет числа {element}!')
        return False

    def replace(self, old_element, new_element, all_el=None):
        if self.head is None:
            print('Список пустой')
            return
        current = self.head
        while current:
            if current.value == old_element:
                current.value = new_element
                if all_el:
                    continue
                else:
                    return
            current = current.next_node

    def __str__(self):
        result = ''
        if self.head is None:
            return 'Список пустой!'
        current = self.head
        while current:
            result += str(current.value) + ' -> '
            current = current.next_node
        result += 'None'
        return result

    def revers_list(self):
        result = []
        if self.head is None:
            return 'Список пустой!'
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next_node
        string = 'None <-'
        string += ' <- '.join(reversed(result))
        return string


s = SingleList()

nums = input('Введите числа через запятую для добавления в список: ')
list_nums = nums.split(', ')

for num in list_nums:
    s.append(int(num))

print(f'Односвязный список из чисел {list_nums}:\n', s)

print('1 - Добавить новое число в список\n'
      '2 - Удалить все вхождения числа из списка\n'
      '3 - Показать содержимое списка\n'
      '4 - Проверить если число в списке\n'
      '5 - заменить значение в списке\n'
      '0 - выход из программы\n')

while True:
    command = input('Введите команду: ')
    if command.isdigit():
        command = int(command)
    else:
        print('Команда должна быть цифрой!!!')
        continue
    if command == 0:
        print('До свидания!')
        break
    elif command == 1:
        num = int(input('Введите число для добавления в список: '))
        s.append_new_num(num)
    elif command == 2:
        num = int(input('Введите число для удаления: '))
        s.delite_all_element(num)
    elif command == 3:
        print('Показать содержимое списка:')
        vol = int(input('1 - с начала\n'
                        '2 - с конца\n'))
        if vol == 1:
            print(s)
        else:
            print(s.revers_list())
    elif command == 4:
        num = int(input('Введите число для проверки: '))
        s.contains(num)
    elif command == 5:
        old = int(input('Введите число для замены: '))
        new = int(input('Введите число на которое будет замена: '))
        vol = int(input('1 - заменить первое вхождение\n'
                        '2 - заменить все вхождения\n'))
        if vol == 1:
            s.replace(old, new)
        else:
            s.replace(old, new, 1)
    else:
        print('Такой команды нет!!!')
