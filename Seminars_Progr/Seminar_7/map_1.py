# функция высшего порядка map(функция, котрую нужно реализовать и аргументы для преобразования)
my_list = ['6', '7', '3', '4']
#my_list = list(map(int, my_list))
my_list = list(map(lambda x:int(x)+2, my_list))
print(sum(my_list))