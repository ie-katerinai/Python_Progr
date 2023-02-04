# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите число: '))
sum = 0
strr = str(n)
for i in strr:
    if (i=="."):
        i = 0
    sum += int(i)
print(sum)


# n * 10
# if n == int(n)

# n = input()
# n = n.replace(',', '')
# n = n.replace(',','')

# n = input()
# n = n.replace(',', '').replace(',','')
# n = int(n)


# sum = 0
# while n > 0:
#    sum += n%10
#    n = n // 10

# n = input()
# n = n.replace(',', '').replace(',','')
# for i in n:
#   if i in '0123456789':
#   if i.isdigit(): проверяте цифра ли
#    sum += int(i)

# print(sum(map(int, list(str(input('Введите число: ')).replace('.','')))))