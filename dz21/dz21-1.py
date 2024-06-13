# Задание 1.
# Создайте реализацию паттерна Command. Протестируйте
# работу созданного класса.

from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommandA(Command):
    def execute(self):
        self.receiver.action_a()


class ConcreteCommandB(Command):
    def execute(self):
        self.receiver.action_b()


class Receiver:
    def action_a(self):
        print('Receiver executing action A')

    def action_b(self):
        print('Receiver executing action B')


class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()


receiver1 = Receiver()
command_a = ConcreteCommandA(receiver1)
command_b = ConcreteCommandB(receiver1)
invoker = Invoker()

invoker.add_command(command_a)
invoker.add_command(command_b)
invoker.execute_commands()
