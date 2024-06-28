import random
import threading

list_numbers = []
event = threading.Event()


def fill_list(nums: list):
    for i in range(30):
        nums.append(random.randint(1, 100))
    print('Список заполнен!!!', list_numbers)
    event.set()


def summa(nums: list):
    event.wait()
    print(f'Сумма чисел в списке: ', sum(nums))


def arithmetic_mean_logical(nums: list):
    event.wait()
    aml = sum(nums) / len(nums)
    print(f'Среднее арифметическое: {aml}')


def main():
    threading1 = threading.Thread(target=fill_list, args=(list_numbers,))
    threading2 = threading.Thread(target=summa, args=(list_numbers,))
    threading3 = threading.Thread(target=arithmetic_mean_logical, args=(list_numbers,))

    threading1.start()
    threading2.start()
    threading3.start()

    threading1.join()
    threading2.join()
    threading3.join()


if __name__ == '__main__':
    main()
