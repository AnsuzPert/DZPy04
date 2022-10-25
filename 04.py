#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#     многочлена и записать в файл многочлен степени k.
#     Пример:



import random
slov = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
per1 = int(input('Введите натуральную степень : '))
file = [random.randint(0, 100) for _ in range(per1 + 1)]
print(file)
with open('file.txt', 'w', encoding='utf-8') as fire:
    for i in range(len(file)):
        if per1 - i != 1 and per1 - i != 0:
            fire.write(f'{file[i]}x{slov[per1 - i]} + ')
        elif per1 - i == 1:
            fire.write(f'{file[i]}x + ')
        elif per1 - i == 0:
            fire.write(f'{file[i]} = 0')