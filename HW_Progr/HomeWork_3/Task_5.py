# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
if n == 0:
    final_list = [0]
elif n == 1:
    final_list = [1, 0, 1]
# print(final_list)
else:
    final_list = [1, 0, 1]
    for i in range(n - 1):
        negafibonachi = final_list[1] - final_list[0]
        final_list.insert(0, negafibonachi)
        fibonachi = final_list[len(final_list) - 2] + final_list[len(final_list) - 1]
        final_list.append(fibonachi)
print(final_list)