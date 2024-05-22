import re

# 1. Напишите регулярное выражение для разбора строк логов определенного формата.
# Например, для строки лога "2024-05-12 12:34:56 [INFO] Сообщение лога" нужно
# извлечь дату, время, уровень логирования и само сообщение.

log = "2024-05-12 12:34:56 [INFO] Сообщение лога"
pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.*)'
match = re.match(pattern, log)
if match:
    print(f'Дата: {match.group(1)}\nВремя: {match.group(2)}\n'
          f'Уровень логирования: {match.group(3)}\nСообщение: {match.group(4)}')

# 2. Напишите регулярное выражение, которое проверит, является ли строка допустимым паролем.
# Пароль считается допустимым, если он содержит как минимум 8 символов, включая
# хотя бы одну строчную букву, одну заглавную букву, одну цифру и один специальный символ.

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

while True:
    print('\nПроверте пароль или введите 0 для выхода!!!')
    password = input('Введите пароль: ')
    if password == '0':
        break
    else:
        if re.match(pattern, password):
            print('Пароль надежный!!!')
        else:
            print('Пароль не надежный!!!')


# 3. Напишите регулярное выражение, которое извлечет данные из HTML-таблицы, включая теги
# <table>, <tr>, <td>, и содержимое ячеек. Например, из строки HTML-таблицы:

table = '<table><tr><td>Ячейка 1</td><td>Ячейка 2</td></tr><tr><td>Ячейка 3</td><td>Ячейка 4</td></tr></table>'

pattern_table = r'<table>.*?</table>'
pattern_tr = r'<tr>.*?</tr>'
pattern_td = r'<td>.*?</td>'

res_table = re.findall(pattern_table, table)
res_tr = re.findall(pattern_tr, table)
res_td = re.findall(pattern_td, table)
print(f'Таблица:', *res_table, sep='\n\t')
print(f'Ряды таблицы:', *res_tr, sep='\n\t')
print(f'Ячейки таблицы:', *res_td, sep='\n\t')

# 4. Напишите регулярное выражение, которое найдет все ссылки в тексте, включая ссылки
# на веб-сайты (http/https), электронные адреса и ссылки на файлы. Затем оберните его
# в функцию, которая возвращает данные в виде словаря:
# {"Ссылки": [...], "Почты": [...], "Файлы": [...]}

text = ('Ссылки на веб-сайты: https://www.google.com, www.youtube.com. Электронные адреса: 123456@gmail.com,'
        'login.3-67@gmail.com. Файлы: C:\ocean\Downloads\dz.zip, D:\Учёба\HTMLCSS\Отступы.html')


def return_dict(string: str) -> dict:
    url = re.findall(r'(?:https?://|www\.)[a-zA-Z0-9.-]+.[a-zA-Z]{2,}', string)
    mail = re.findall(r'[\w.-]+@[\w.]*mail\.(?:ru|com)', string)
    file = re.findall(r'[A-Z]:[a-zA-Z0-9а-яА-Яё\-.\\]+.[a-zA-Z]{2,}', string)
    return {'Ссылки:': url,
            'Почты:': mail,
            'Файлы:': file}


print(return_dict(text))
