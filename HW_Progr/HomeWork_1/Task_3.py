# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка.
# Пример:
# - x = 34; y = -30 -> 4
# - x = 2; y = 4 -> 1
# - x = -34; y = -30 -> 3

x = int(input('Введите значение координаты x: '))
y = int(input('Введите значение координаты y: '))
if (x == 0 or y == 0):
    print('Значеия координат не должны равняться 0!')
else:
    if (x > 0 and y > 0): print('Точка (',x,',',y,') находится в I четверти')
    elif (x < 0 and y > 0): print('Точка (',x,',',y,') находится в II четверти')
    elif (x < 0 and y < 0): print('Точка (',x,',',y,') находится в III четверти')
    else: print('Точка (',x,',',y,') находится в IV четверти')