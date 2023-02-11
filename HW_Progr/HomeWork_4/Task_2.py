# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число: '))
divider_list = []
for i in range(2, n + 1):
    if n % i == 0:
        divider_list.append(i)
print(divider_list)


def find_simple_divider(number):
    count = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            count += 1
    if count > 2:
        return False
    else:
        return True

final_list = []
k = 0

for k in range(len(divider_list)):
    if (find_simple_divider(divider_list[k])):
        final_list.append(divider_list[k])
print(final_list)