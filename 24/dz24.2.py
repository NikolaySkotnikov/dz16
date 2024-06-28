import random
import threading

event = threading.Event()


def fill_file(path):
    with open(path, 'w', encoding='utf-8') as file:
        nums = [random.randint(1, 100) for i in range(20)]
        file.write(', '.join([str(i) for i in nums]))
    event.set()


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def prime_number(path):
    event.wait()
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    nums = data.split(', ')
    prime = [int(i) for i in nums if is_prime(int(i))]
    with open('prime numbers.txt', 'w', encoding='utf-8') as file:
        file.write(', '.join([str(i) for i in prime]))


def factorial_numbers(path):
    event.wait()
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
    nums = data.split(', ')
    factorial_nums = [factorial(int(i)) for i in nums]
    with open('factorial numbers', 'w', encoding='utf-8') as file:
        file.write(', '.join([str(i) for i in factorial_nums]))


def main():
    path_to_file = input('Введите путь к файлу: ')

    threading1 = threading.Thread(target=fill_file, args=(path_to_file, ))
    threading2 = threading.Thread(target=prime_number, args=(path_to_file, ))
    threading3 = threading.Thread(target=factorial_numbers, args=(path_to_file, ))

    threading1.start()
    threading2.start()
    threading3.start()

    threading1.join()
    threading2.join()
    threading3.join()


if __name__ == '__main__':
    main()
