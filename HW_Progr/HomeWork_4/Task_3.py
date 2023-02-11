# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

text =input('Введите числа: ')
numbers_list = text.split()
print()
numbers = set(numbers_list)
print(*sorted(numbers))


