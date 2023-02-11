# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random

k = int(input('Введите натуральную степень многочлена: '))
result = ''
for i in range(k+1):
    coef = random.randint(1,100)
    if i != 0:
        result = (f'{coef} * x^{i} + ') + result
    else: result = result + (f'{coef} = 0')
print(result)
