number = int(input('Enter number: '))
sum = 0
while number > 0:
    x = number % 10
    sum = sum + x
    number //= 10
print(sum)