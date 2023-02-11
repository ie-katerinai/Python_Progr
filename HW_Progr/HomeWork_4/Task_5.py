# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def read_file(file_name):
    # list_1 = []
    f = open('/Users/evahome/Documents/Python_Progr/HW_Progr/HomeWork_4/'+ file_name, 'r')
    for line in f:
        result = str(line)
    return result

def split_string(initial_string):
    new_list = initial_string.split('+')
    return new_list

# def find_x(initial_string):
#     new_list = initial_string.split('x')
#     return new_list

def find_sign(initial_list):
    new_list = []

    for i in range(len(initial_list)):
        if (i == '-'):
            new_list.append('-' + i + 1)
        else: new_list.append(i)

str_1 = 'File_1.txt'
str_2 = 'File_2.txt'
f = str(read_file(str_1))
k = str(read_file(str_2))
print(split_string(f), split_string(k))
print(find_sign(f))


