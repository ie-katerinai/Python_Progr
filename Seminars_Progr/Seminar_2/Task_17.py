# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# inputList = [1, 1, 2, 0, -1, 3, 4, 4]
# countList = {}

# for i in inputList:
#     countList[i] = inputList.count(i)

# print(inputList)
# print(len(countList))

inputList = [1, 1, 2, 0, -1, 3, 4, 4]
countList = []

for i in inputList:
    if countList.count(i) == 0:
        countList.append(i)

print(inputList)
print(len(countList))



inputList = [1, 1, 2, 0, -1, 3, 4, 4]
print(inputList)
print(len(set(inputList)))