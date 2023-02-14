# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                              Вывод:
# 7                                 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# решение в группе
list_1 = [int(i) for i in input().split()]
list_2 = [int(i) for i in input().split()]
new_list = []
for el in list_1:
    if el not in list_2:
        new_list.append(el)
print(new_list)



# решение с преподавателем


def sort_of_digits(lisst1, lisst2):
    final_list = []
    for i in range(len(first_list)):
        if first_list[i] not in second_list:
            final_list.append(first_list[i])
    return final_list

first_list = [3, 1, 3, 4, 2, 4, 12]
second_list = [4, 15, 43, 1, 15, 1]
print(sort_of_digits(first_list, second_list))


# решение через множество
def sort_of_digits(list_1, list_2):
    final_list = []
    list_2 = set(list_2)
    for i in range(len(list_1)):
        final_list.append(list_1[i])
    return final_list

list_1 = [3, 1, 3, 4, 2, 4, 12]
list_2 = [4, 15, 43, 1, 15, 1]
print(sort_of_digits(list_1, list_2))
