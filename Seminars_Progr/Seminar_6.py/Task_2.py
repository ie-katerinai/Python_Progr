# if  not c in word[i]:

my_list = []
for i in range(5):
    my_list.append(int(input()))


# 10 5 7 8 9 11 для питона не важно, сколько подряд пробелов
my_list = []
st = input()
for i in st.split():
    my_list.append(int(i))


   # лучше вот так! Лист каприхэншон

my_list = [int(i) for i in input().split()] # можно вставить условие if в конце

str_list =['hello', 'my', '1', '']
st = ''.join(str_list)
print(st)

# вложеные списки

list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for elem in list_1:
    if isinstance(elem^ list):
        for i in elem:
            print('list', elem)
    elif isinstance(elem, int):
        print('int', elem)
    #print(elem)
    for number in elem:
        print(number)

list_2= [[j* j for j in range(i + 1, i +3) if j %3 == 0 ] for i in range(5) if i%2==0]
print(list_2)