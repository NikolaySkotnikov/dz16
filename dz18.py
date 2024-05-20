# 1. Напишите регулярное выражение, которое соответствует всем строкам,
# начинающимся с гласной и заканчивающимся на согласную.

import re

print('\n1 задание.\n')

test_string = ('Loremm ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt '
               'ut labore et dolore magna aliqua. Elit eget gravida cum sociis natoque penatibus et magnis '
               'dis. Enim tortor at auctor urna nunc. Mauris pharetra et ultrices neque. Tristique nulla aliquet '
               'enim tortor at. Condimentum lacinia quis vel eros donec ac odio. Non arcu risus quis varius quam. '
               'Risus quis varius quam quisque id diam. Imperdiet dui accumsan sit amet nulla. Egestas quis ipsum '
               'suspendisse ultrices gravida dictum fusce ut placerat. Turpis in eu mi bibendum neque egestas congue. '
               'Egestas maecenas pharetra convallis posuere. Quisque non tellus orci ac auctor augue mauris. '
               'Duis ultricies lacus sed turpis tincidunt id aliquet. Accumsan in nisl nisi scelerisque eu ultrices '
               'vitae auctor eu. Quam viverra orci sagittis eu volutpat odio facilisis mauris sit. Sem nulla pharetra '
               'diam sit amet nisl suscipit adipiscing bibendum. Aras ornare arcu dui vivamus arcu felis. Tellus cras '
               'adipiscing enim eu turpis egestas prettium aenean pharetra. A condimentum vitae sapien pellentesque '
               'habitant morbi tristique.')

test_list = re.split('\.\s?|!\s?|\?\s?', test_string)
pattern = r'^[AEIOU].*[bcdfghjklmnpqrstvwxyz]$'

for string in test_list:
    if re.match(pattern, string):
        print(string + '.')


# 2. Напишите регулярное выражение, которое соответствует всем URL - адресам.

print('\n2 задание.\n')

adress = 'https://www.google.com, http://www.youtube.com,  www.google.com, www.youtube.com, pretium aenean pharetra'
pattern = r'(?:https?:\/\/|www\.)[a-zA-Z0-9.-]+.[a-zA-Z]{2,}'
print(re.findall(pattern, adress))

# 3. Напишите регулярное выражение, которое соответствует всем строкам,
# содержащим хотя бы одно слово, начинающееся с заглавной буквы.

print('\n3 задание.\n')

pattern = r'\b[A-Z][a-z]*\b'
for string in test_list:
    if re.match(pattern, string):
        print(string + '.')

# 4. Напишите регулярное выражение, которое соответствует всем строкам, содержащим повторяющуюся букву
# (например, book или letter).

print('\n4 задание.\n')

pattern = r'\b\w*?(\w)(?=\1)\w*?\b'
for string in test_list:
    if re.match(pattern, string):
        print(string + '.')

