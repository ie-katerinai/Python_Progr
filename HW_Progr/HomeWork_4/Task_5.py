# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def read_file(file_name):
    f = open('/Users/evahome/Documents/Python_Progr/HW_Progr/HomeWork_4/'+ file_name, 'r')
    for line in f:
        result = str(line)
    return result

def split_string(initial_string):
    list_1 = initial_string.split('+')
    list_2=[]
    for i in range(len(list_1)):
        list_2.append(list_1[i].strip())
    list_3 = list_2[len(list_2)-1].split()
    list_2[len(list_2)-1] = list_3[0]
    list_4 = []
    for i in range(len(list_2)):
        list_4.append(list_2[i].split('*'))
    return list_4

def summa_multiple(str_1, str_2):
    result = []
    for i in range(len(str_1)):
        result.append(str_1[i,0]+str_2[i, 0])
    return result

str_1 = 'File_1.txt'
str_2 = 'File_2.txt'
f = str(read_file(str_1))
k = str(read_file(str_2))
print(split_string(f), split_string(k))
print(summa_multiple(split_string(f), split_string(k)))


