def hello(name):
    print('hello')
    print('my friend,', name)

hello('Petya')
hello('Vasya')



def hello(name, daytime='morning'):
    st = ''
    if daytime == 'morning':
        st = st + 'Доброе утро'
    st = st + name
    print('hello')
    print('my friend,', name)
    return

hello('Petya','morning')
hello('Vasya')
print(hello('Вася'))


import math
print(math.sqrt(4))