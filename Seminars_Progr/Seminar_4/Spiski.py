# my_dict = {'cat': 'rjirf', 'dog': 'cj,frf', 'nice': '[jhjibq'}
# for key in my_dict:
#     print( key, my_dict[key])

# my_list = list(my_dict.items())
# print(my_list)
# for elem in my_list:
#     print(elem)
#     print(elem[0], elem[1])



# list comprehension
   
# a= []
# for i in range(10):
#     a.append(i)

begin = time.time()

a = [i for i in range(10) if i%2 == 0] #- заполнить четными числамт
print(a)

a = [i for i in range(100) if i%2 == 0] #- заполнить четными числамт
print(a)
b = [(i, i*i) for i in a if i%3 ==0] #- числа делятся на 3 и вывод в виде кортежей квадрата числа
my_dict = {i: i**2 for i in range(10)}
print(b)
end = time.....
# python -m cProfile -s time prof.py 10001