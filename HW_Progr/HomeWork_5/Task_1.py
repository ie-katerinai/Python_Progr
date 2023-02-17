# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = str(input('Введите текст: '))
#text = 'абвра кадабра швабвра'
list_1 = text.split()
list_2 = []
for i in range(len(list_1)):
    index = list_1[i].find('абв')
    if index == -1:
        list_2.append(list_1[i])
print(*list_2)