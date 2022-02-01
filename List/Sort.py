my_list = input("Enter the numbers seperating with space : ").split()

for i in range(0, len(my_list)):
    my_list[i] = int(my_list[i])

my_list.sort()

print(my_list[0])
