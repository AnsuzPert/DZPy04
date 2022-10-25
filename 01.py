#     Вычислить число c заданной точностью d
#     Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


per1 = float(input('ВВедите основное число: '))
per2 = float(input('ВВедите точность: '))
if per2 ==1:
    print (int(per1))
else:
    per2 = str(per2)
    per2 = per2.split('.')
    per2 = len(per2[1])
    print (per2)
    print (round(per1, per2))
