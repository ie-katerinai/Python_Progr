# Создайте программу для игры в ""Крестики-нолики"".
import random

my_symbol = input('Выберите сторону X или O: ')
my_symbol = my_symbol.upper()
if my_symbol == 'X':
    bot_symbol = 'O'
elif my_symbol == 'O':
    bot_symbol = 'X'
else: print ('Некорректный ввод')
play_field = {1:'', 2:'', 3:'', \
            4:'', 5:'', 6:'', \
            7:'', 8:'', 9:''}

def make_turn(symbol, field): 
    move = int(input('Сделайте ваш ход от 1 до 9: '))
    if check_win(field):
        print('Game over')
    else:
        while not check_turn(move, field):
            move = int(input('Ячейка занята. Сделайте ваш ход от 1 до 9 заново: '))
            if check_win(field):
                print('Game over')
        field = insert_turn(move, symbol, field)
    return field

def make_bot_turn(symbol, field):
    bot_move = random.randint(1, 9)
    if check_win(field):
        print('Game over')
    else:
        while not check_turn(bot_move, field):
            bot_move = random.randint(1, 9)
            if check_win(field):
                print('Game over')
        field = insert_turn(bot_move, symbol, field)
    return field

def check_turn(turn, field):
    if field[turn] == '':
        return True
    else: return False

def insert_turn(turn, simbol, field):
    field[turn] = simbol
    return field

def check_win(field):
    rule1 = (field[1] == 'X') & (field[2] == 'X') & (field[3] == 'X')
    rule2 = (field[4] == 'X') & (field[5] == 'X') & (field[6] == 'X')
    rule3 = (field[7] == 'X') & (field[8] == 'X') & (field[9] == 'X')
    rule4 = (field[1] == 'X') & (field[4] == 'X') & (field[7] == 'X')
    rule5 = (field[2] == 'X') & (field[5] == 'X') & (field[8] == 'X')
    rule6 = (field[3] == 'X') & (field[6] == 'X') & (field[9] == 'X')
    rule7 = (field[1] == 'X') & (field[5] == 'X') & (field[9] == 'X')
    rule8 = (field[3] == 'X') & (field[5] == 'X') & (field[7] == 'X')
    rule11 = (field[1] == 'X') & (field[2] == 'X') & (field[3] == 'X')
    rule12 = (field[4] == 'X') & (field[5] == 'X') & (field[6] == 'X')
    rule13 = (field[7] == 'X') & (field[8] == 'X') & (field[9] == 'X')
    rule14 = (field[1] == 'X') & (field[4] == 'X') & (field[7] == 'X')
    rule15 = (field[2] == 'X') & (field[5] == 'X') & (field[8] == 'X')
    rule16 = (field[3] == 'X') & (field[6] == 'X') & (field[9] == 'X')
    rule17 = (field[1] == 'X') & (field[5] == 'X') & (field[9] == 'X')
    rule18 = (field[3] == 'X') & (field[5] == 'X') & (field[7] == 'X')
    if (rule1 | rule2 | rule3 | rule4 | rule5 | rule6 | rule7 | rule8 | rule11 | rule12 | rule13 | rule14 | rule15 | rule16 | rule17 | rule18):
        return True
    else: return False

for x in range(1, 10):
    play_field = make_turn(my_symbol, play_field)
    print(play_field)
    if check_win(play_field):
        print('Game Over! You WIN')
        break
    play_field = make_bot_turn(bot_symbol, play_field)
    print(play_field)
    if check_win(play_field):
        print('Game Over! Bot WIN')
        break
    
        
        