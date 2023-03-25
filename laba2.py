# Натуральные числа. Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр.
# Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

import re
# словарь с прописными цифрами
digits = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

K = 3
with open('data.txt') as input_file:
    buffer = input_file.readline().split()
    pattern = r"^[0-9|\"]\d*(\d)\1{%d,}\d*[$\d|\"|?|!]" % K
    for item in buffer:
        for match in re.finditer(pattern, item):
            num = match.group(0)
            for ch in ['"', "?", "!"]:
                if ch in num:
                    num = num.replace(ch,'')
            print(num + ' ' + digits[match.group(1)] + ' ' + str(match.group(0).count(match.group(1))))
