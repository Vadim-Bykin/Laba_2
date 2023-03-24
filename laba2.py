# Натуральные числа. Выводит на экран числа, содержащие хотя бы одну последовательность длиннее К подряд идущих одинаковых цифр.
# Рядом с таким числом выводится повторяющаяся цифра (прописью) и количество повторений.

import re
# словарь с прописными цифрами
digits = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
K = 3
with open('text.txt', 'r') as input_file:
    while True:
        a = input_file.readline().split() # читаем строку
        if not a: # если файл пустой
            print("Файл *.txt в директории проекта кончился")
            break
        # цифры 0 или более раз группа повторяющихся цифр, потом может идти опять группа любых цифр, учитываем \s слева и справа - граница слова
        pattern = r'\d*(\d)\1{%d,}\d*' % K  # шаблон для поиска последовательностей подходящих под условие задачи
        for match in re.finditer(pattern, a):  # перебираем все подходящие под шаблон последовательности
            repeated_dig = match.group(1)  # повторяющаяся цифра лежит в group(1)
            pattern_repeat = r'([' + repeated_dig + '])\\1{%d,}' % K  # шаблон для поиска только повторяющихся последовательностей в найденной последовательности для подсчета количества повторяющихся цифр   
            count_repeat = len(re.search(pattern_repeat, match.group(0)).group(0))  # количество повторяющихся цифр в match.group(0) - в исходной поседовательности
            # здесь после обработки search - в group(0) лежит последовательность только из повторяющихся цифр
            print(match.group(0) + ' ' + digits[match.group(1)] + ' ' + str(count_repeat))  # результат
