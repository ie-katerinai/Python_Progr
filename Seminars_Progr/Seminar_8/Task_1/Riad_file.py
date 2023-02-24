def 
    file = open('/Users/evahome/Documents/Python_Progr/Seminars_Progr/Seminar_8/Task_1/spravochnik.txt', 'r', encoding='utf-8') 
    stroki = file.readlines()
    print(stroki)
    file.close()