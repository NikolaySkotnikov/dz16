import os
import threading


event = threading.Event()


def merging_files(dir, word):
    list_file = os.listdir(dir)
    result = ''
    for file in list_file:
        with open(dir + '\\' + file, 'r', encoding='utf-8') as f:
            data = f.read()
            print(data.lower())
            if word.lower() in data.lower():
                result += (data + '\n')
    with open('merging files.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    event.set()


def cut_words():
    event.wait()
    result = []
    with open('words.txt', 'r', encoding='utf-8') as file:
        words = file.read().split(', ')
    with open('merging files.txt', 'r', encoding='utf-8') as file:
        text = file.read().split()
    for t in text:
        if t.lower() not in [i.lower() for i in words]:
            result.append(t)
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(result))


def maim():
    directory = input('Введите путь к директории: ')
    word_for_file = input('Введите слово для поиска: ')

    threading1 = threading.Thread(target=merging_files, args=(directory, word_for_file))
    threading2 = threading.Thread(target=cut_words)

    threading1.start()
    threading2.start()

    threading1.join()
    threading2.join()


if __name__ == '__main__':
    maim()
