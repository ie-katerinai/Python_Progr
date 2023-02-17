# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def zipper(text):
    final_str = ''
    count = 1
    previous = ''
    for current in text:
        if current != previous:
            if previous:
                final_str += str(count) + previous
            previous = current
            count = 1
        else:
            count += 1
    else:
        final_str = final_str + str(count) + previous
    return final_str

def unzipper(text):
    final_str = ''
    number = 1
    for simbol in text:
        if simbol.isdigit():
            number = int(simbol)
        else: final_str += simbol * number
    return final_str

text = input('Введите текст для сжатия или распаковки: ')
letter = text[0]
if letter.isdigit():
    print(unzipper(text))
elif letter.isalpha():
    print(zipper(text))
else: print('Некорректный ввод')