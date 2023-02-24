def read_data():
    with open('49\\data.txt', 'r', encoding='utf-8') as file:
        my_list = file.readlines()
        return(my_list)
    
def print_data(my_list):
    for i in my_list:
        print(i.strip())
        
def add_user(my_list):
    my_list.append('\n' + input("Добавьте пользователя: "))
    
def write_data():
    with open('49\\data.txt', 'w', encoding='utf-8') as file:
        file.writelines(my_list)
        
def search_data():
    text = input('Введите текст для поиска: ')
    for elem in my_list:
        if text in elem:
            print(elem.strip())

my_list = read_data()
print_data(my_list)
add_user(my_list)
print_data(my_list)
write_data()
search_data()