my_list =map(int, input().split())
print(list(my_list))

my_list_2 =list(map(list(map(int, input().split()))))
print(my_list_2)