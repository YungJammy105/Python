import random

n = int(input('Enter the number of bushes from 3 pcs: '))
while n < 3:
    n = int(input('Enter the number of bushes from 3 pcs: '))
k = random.randint(1, 100)
list_k = [random.randint(1, 10) for i in range(k)]
max_k = list_k[-1] + list_k[0] + list_k[1]
for i in range(1, len(list_k) - 1):
    temp = list_k[i - 1] + list_k[i] + list_k[i + 1]
    if max_k < temp:
        max_k = temp
if max_k < list_k[-1] + list_k[-2] + list_k[0]:
    max_k = list_k[-1] + list_k[-2] + list_k[0]
print(*list_k)
print(max_k)