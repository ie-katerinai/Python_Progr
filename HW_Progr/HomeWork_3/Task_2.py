# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите количество элементов списка: '))
list_1 = []
for i in range(n):
    list_1.append(int(input('-->')))
print(list_1)
list_2 = []
f = None
if n % 2 == 0:
    for k in range(n//2):
        f = list_1[k] * list_1[len(list_1) - 1 - k]
        list_2.append(f)
else:
    for k in range(n//2 + 1):
        f = list_1[k] * list_1[len(list_1) - 1 - k]
        list_2.append(f)
print(list_2)
