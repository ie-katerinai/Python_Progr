# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
list_str = ""
while n > 0:
    if n % 2 == 0:
        list_str = '0' + list_str
    else:
        list_str = '1' + list_str
    n= n//2
print(list_str)
