# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_marks(mark_list):
    maximal_marks = max(mark_list)
    minimal_marks = min(mark_list)
    for i in range(len(mark_list)):
        if (mark_list[i] == maximal_marks):
            mark_list[i] = minimal_marks
    return mark_list

numbs = int(input('Введите количество оценок Василия: '))
marks_list = []
for i in range(numbs):
    marks_list.append(input('--->'))
print('Оценки Василия: ',*marks_list)
print('Новые оценки Василия: ', *change_marks(marks_list))