summa = 0
current_number = 1
while current_number < 11:
    summa += current_number
    current_number += 2
    #break этот цикл работает, если программа сама закончила цикл while
else:
    print('bye')
print(summa)