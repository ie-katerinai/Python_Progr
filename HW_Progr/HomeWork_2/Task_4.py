# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
list = []
i = -n
while i <= n:
    list.append(i)
    i += 1
print(list)
list_2 = []
f = open('/Users/evahome/Documents/Python_Progr/HW_Progr/HomeWork_2/file.txt', 'r')
for line in f:
    list_2.append(int(line))
print(list_2)
sum = 1
for k in list_2:
    sum = sum * list[k]
print(sum)