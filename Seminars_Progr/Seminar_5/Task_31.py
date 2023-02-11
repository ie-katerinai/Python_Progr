# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
#  a0 = 0, a 1= 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fibonachi(i):
#     if i == 0:
#         return 0
#     elif i in [1, 2]:
#         return 1
#     return fibonachi(i - 1) + fibonachi(i - 2)

# n = int(input('Введите число:'))
# for i in range(25):
#     print(i, fibonachi(i))
#print(fibonachi(n))


a = [1,1]
for i in range(2, 100):
    a.append(a[i-1]+a[i-2])
print(a)