# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
i = 1
sum = 0
while i <= n:
    sum = sum + (1 + 1/i)**i
    i += 1
print(round(sum, 3))