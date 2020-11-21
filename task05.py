# 5. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

dict = {}

# Сложность этого задания в том, что рядом с числами находятся строки (пр), (л), (лаб).
# Для поиска чисел в строке, я решил использовать библиотеку для работы с регулярными выражениями(import re)
# В разборе ДЗ мне кажется посложней, чтобы найти число, там используют срез с поиском открывающейся скобки.

with open('task05.txt', 'r') as f:
    for line in f: #построчно перебираем файл
        line_lst = line.split(' ') #получаем список в виде: ['Информатика:', '100(л)', '50(пр)', '20(лаб)\n']
        num_tasks = re.findall('(\d+)', line) # С помощью регулярного выражения, ищем в строке только числа. Итого в num_tasks получаем список ['100', '50', '20']
        sum_tasks = sum(map(int, num_tasks)) #суммируем элементы списка
        dict.update({line_lst[0].rstrip(':'): sum_tasks}) #Добавляем в словарь ключ "Информатика:"(line_lst[0]), через .rstrip(':') убрав двоеточие на конце, в значение идёт полученная выше сумма занятий.

print(dict)