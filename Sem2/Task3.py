import os

os.system('CLS')
num_sum = int(input('Enter the sum of the numbers: '))
product = int(input('Enter of product numbers: '))
num_x = num_sum // 2
num_y = num_sum // 2

while (num_y < num_sum):
    if (num_x + num_y == num_sum):
        if (num_x * num_y == product):
            print(num_x, num_y)
            break
    num_x -= 1
    num_y += 1
if (product // num_y != num_x):
    print('Numbers not found!')