# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = ("She sells sea shells on the sea shore " +
"The shells that she sells are sea shells " +
"I'm sure. So if she sells sea shells on the sea shore " +
"I'm sure that the shells are sea shore shells")
#print(len(set(text.replace('.', '').lower().split())))
text = text.replace('.', '').lower()
my_list = text.split()
print(my_list)
print()
my_set = set(my_list)
print(len(my_set))

# my_list = st.split(' ')
# print(my_list)
# print()
# my_set = set(my_list)
# print(my_set)
# my_list.sort()
# print(my_list)