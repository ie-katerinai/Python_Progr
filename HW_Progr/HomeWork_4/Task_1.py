# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   10**(-1) ≤ d ≤10**(-10)



def pi_calculated(number):
    for i in (1, number+1, 4):
        pi = 4
        pi = pi - 4/(i + 2) + 4/(i + 4)
    return pi

d = input('Задайте точность от 0.1 до 0.0000000001: ')
count_numbs = len(d) - 2
print(round(pi_calculated(count_numbs)), count_numbs)