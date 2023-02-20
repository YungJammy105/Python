import random

def randomgenlist(min,max,len):
    list = [random.randint(min, max) for i in range(len)]
    return list

length_list = int(input('Enter list length: '))
my_list = randomgenlist(1,20,length_list)
print(*my_list)
repeating_num = int(input('Enter number: '))
count_num = 0
for i in range(len(my_list)):
    if my_list[i] == repeating_num:
        count_num += 1
print(f'The number is repeated {count_num} times')

