# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
mult = 1
i = 1
list_1= []
while i <= n:
    mult = mult * i
    i += 1
    list_1.append(mult)
print(list_1)