# обычная функция
def sum(x, y):
    return x + y
# сокращенный вариант
sum = lambda x, y: x + y
#sum = lambda x, y: x + y 'yes' if x == y else 'no'
print(sum(5,6))

def summa(a, b):
    return a + b

def calc(a, b, operation):
    return operation(a, b)

print(calc(4, 6, summa)) # функция высшего порядка - в качестве аргумента ей передается другая функция

