# Реализуйте алгоритм перемешивания списка.
import random
n = int(input('Введите длину списка: '))
list = []
i = 0
while i < n:
    list.append(random.randint(1,100))
    i += 1
print(list)
random.shuffle(list)
print(list)