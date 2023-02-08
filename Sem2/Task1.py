import os

os.system('CLS')
count_watermelon = int(input('Enter count watermelon!: '))
arr = []
for i in range(count_watermelon):
    arr.append(int(input(f'Enter weight {i + 1} watermelon: ')))
min = arr[0]
max = arr[0]
for i in range(len(arr)):
    if (max < arr[i]):
        max = arr[i]
    elif (arr[i] < min):
        min = arr[i]
print(arr)
print(f'Minimal weight watermelon = {min}! \nMaximum weight watermelon = {max}!')
