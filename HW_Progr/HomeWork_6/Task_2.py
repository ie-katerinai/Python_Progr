# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
list_1 = [int(i) for i in input().split()]
print(list_1)
for i in range(len(list_1)):
    if a <= list_1[i] <= b:
        print(i)