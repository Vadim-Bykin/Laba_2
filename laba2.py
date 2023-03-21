# Натуральные числа. Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр.
# Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

import re

# словарь с прописными цифрами
digits = {
    '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
    '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
}

k = int(input('Введите число k: '))
numbers = []  # список с найденными в последовательности числами

with open('data.txt', 'r') as input_file:
    for row in input_file:  # читаем данные из файла
        cur_number = ''
        for letter in row:
            if letter in digits.keys() or letter == '-':
                cur_number += letter
            else:
                # добавляем в список только числа длиннее k символов,не начинающиеся на 0
                # меньше k гарантированно не подходят под условие задачи
                if cur_number != '' and len(cur_number) > k and (not cur_number.startswith('0')) and (not cur_number.startswith('-')):
                    numbers.append(cur_number)
                cur_number = ''

output_data = ''
for num in numbers:
    match = re.compile(r'(\d)\1{%d,}' % (k))  # регулярное выражение
    for match in match.finditer(num):  # итератор по найденным совпадениям в строке
        pattern = match.group()  # найденные группы одинаковых цифр длиной > k
        result = num + f' {digits[pattern[0]]} {len(pattern)}'  # строка - число в котором найдены повторения + цифра прописью с количеством повторений
        output_data += result+'\n'

if not output_data:
    print('В файле нет чисел, подходящих под условие')
else:
    print('Результат:')
    print(output_data)
