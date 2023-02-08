import math
import os

os.system('CLS')
n = int(input('Enter number: '))
for i in range(n):
    if (math.pow(i, 2) <= n):
        print(i)
