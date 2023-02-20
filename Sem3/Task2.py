import random


def randomgenlist(min, max, len):
    list = [random.randint(min, max) for i in range(len)]
    return list


length = int(input('Enter list lenght: '))
my_list = randomgenlist(1, 100, length)
print(*my_list)
search_num = int(input('Enter search number: '))
find_num = 0
diff = max(my_list)

for i in range(len(my_list)):
    if search_num == my_list[i]:
        print(f'Your number {my_list[i]} is on the list')
        break
    elif search_num > my_list[i]:
        diff_second = search_num - my_list[i]
    elif search_num < my_list[i]:
        diff_second = my_list[i] - search_num

    if diff > diff_second:
        diff = diff_second
        find_num = my_list[i]
print(f'The closest number to {search_num} in the list is {find_num}')
