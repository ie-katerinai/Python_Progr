file = open('/Users/evahome/Documents/Python_Progr/Seminars_Progr/Seminar_8/Rabota_s_file/1.txt', 'r', encoding='utf-8') #- если русский текст
#file = open('1.txt', 'r') # открыть файл
# stroka = file.readline() # считывание построчно, вторую строку можно считать в другую переменную
# stroka = file.readline()
stroki = file.readlines() # считывает весь файл в один лист
#text = file.read() # считали в одну строку
#print(stroka)
print(stroki)
#print(int(stroki[0]))
file.close() # закрыть файл

