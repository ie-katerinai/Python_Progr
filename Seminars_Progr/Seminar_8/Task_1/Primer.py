def menu():
    pass

def change_data():
    pass

def write_data():
    pass

def read_data():
    with open('fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def screen(data):
    for elem in data:
        print(elem)

def main():
    data = read_data()
    screen(data)

if __name__ == '__main__':
    main()