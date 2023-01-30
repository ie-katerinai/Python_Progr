# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if  и циклами.

'''
Первый вариант:

import math
n = int(input('введите n '))
m = int(input('введите m '))
s = m/n
print(math.ceil(s))
'''

'''
Второй вариант: 

n = int(input('Скорость в день: '))
m = int(input('Расстояние км: '))

t = m//n
ostatok = (m % n) > 0
ostatokBool = bool(ostatok)
ostatokDays = int(ostatok)

print('Дней ', t + ostatokDays)
'''

n = int(input('введите n '))
m = int(input('введите m '))
print(round(m/n + 0.4))