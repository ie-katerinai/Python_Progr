# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Введите количество элементов списка: '))
list_1 = []
for i in range(n):
    list_1.append(float(input('-->')))
print(list_1)
list_2 = []
for k in range(n):
    r =round((list_1[k] % 1), 3)
    if r != 0:
        list_2.append(r)
max_remainder = max(list_2)
min_remainder = min(list_2)
print(round((max_remainder - min_remainder), 3))