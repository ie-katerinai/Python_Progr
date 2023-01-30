# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите значение x 0 или 1: '))
y = int(input('Введите значение y 0 или 1: '))
z = int(input('Введите значение z 0 или 1: '))
if (x == 0 or x == 1) and (y == 0 or y == 1) and (z == 0 or z == 1):
    x = bool(x)
    y = bool(y)
    z = bool(z)
    if not (x or y or z) == ((not x) and (not y) and (not z)):
        print('Утверждение верно')
    else:
        print('Утверждение не верно')
else:
    print('Некорректный ввод')
