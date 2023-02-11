def summa(a, b):
    c = a + b
    return c

a = int(input())
b = int(input())
print('Summs = ', summa(a, b))


def summa(*args):  # когда точно не знаем, сколько аргумениов передаем
    print(args)
    s = sum(args)
    # for i in args:
    return s

q = int(input())
w = int(input())
print('Сумма = ', summa(q, w, 5, 4, 2))



def summa():
    # a = 1 #локаоьная а
    b = a + 1
    return b

a = 5 #глобальная а
n = summa()
print(n)


# именованые и порядковые переменные
def summa(*args, **kwargs):
    a, *b, c = args
    print(a,c)
    print(b)
    #print(args)
    print(kwargs)
    return 0

n = (summa(1, 2, 3, 4, 5, name = 'Vasya', key = 'sorted'))