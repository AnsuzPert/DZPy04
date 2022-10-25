# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
per1 = int(input('ВВедите целое число: '))
spis =[]
s = 0
for i in range(2, per1//2+1):
    if per1%i==0:
        for j in range(2, i//2+1):
            if i%j==0:
                s +=1
        if s==0:
            spis.append(i)
        s = 0
print (spis)
