import random
import os

os.system('CLS')
n = int(input('Enter number: '))
arr = [random.randint(0, 1) for i in range(n)]
eagle = 0
tails = 0
for i in range(len(arr)):
    if (arr[i] == 0):
        eagle += 1
    else:
        tails += 1
print(arr)
print(f'There are {eagle} heads and {tails} tails on the table')
if (eagle > tails):
    print(f'You need to flip {len(arr) - eagle} coins so that they are all on the same side')
else:
    print(f'You need to flip {len(arr) - tails} coins so that they are all on the same side')
