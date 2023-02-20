import random


def randomgenlist(min, max, len):
    list = [random.randint(min, max) for i in range(len)]
    return list


first_length = int(input('Enter length first list: '))
first_list = randomgenlist(1, 100, first_length)
second_length = int(input('Enter length second list: '))
second_list = randomgenlist(1,100,second_length)
repeating_num_set = set()
print(*first_list)
print(*second_list)

for i in range(len(first_list)):
    for j in range(len(second_list)):
        if first_list[i] == second_list[j]:
            repeating_num_set.add(first_list[i])

if len(repeating_num_set) == 0:
    print('There are no identical values in the lists')
else:
    print(sorted(repeating_num_set))

