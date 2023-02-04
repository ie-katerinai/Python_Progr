# my_list = [1, 4, 6, 8, 4, 3]
# max_elem = 0
# for i in range(6):
#     if my_list[i] > max_elem:
#         max_elem = my_list[i]
#     print(my_list[i])
# print(max_elem)

# print(max(my_list)/len(my_list)) # среднее арифметическое
# print(min(my_list))
# print(sum(my_list))

# my_list_2 = []
# for i in range(10):
#     num = int(input())
#     my_list_2.append(num)
#     #my_list_2.append(i*i)
# print(my_list_2)

# my_list = [1, 4, 9, 43]
# print(my_list)
# my_list.insert(2, 45)
# print(my_list)

my_list = [1, 2, 4, 'hello', 4, 'abba']
my_tuple = (1, 2, 4, 'hello', 4, 'abba')

stroka = []
chisla = []
for elem in my_list:
    if type(elem) == int:
        chisla.append(elem)
    else:
        stroka.append(elem)
print(stroka)
print(chisla)


a = my_list.copy()

print(my_list.count(4)) # скольео раз встречаеся элемент

ef = list('abrakadabra') # разберет по букве