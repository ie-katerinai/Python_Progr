my_list = ['hello\n', 'bye\n','goodbye\n', 'idea']
with open('/Users/evahome/Documents/Python_Progr/Seminars_Progr/Seminar_8/Rabota_s_file/1.txt','w', encoding='utf-8') as file:
    file.writelines(my_list)