def numsun(a, b):
    a += 1
    if b == 1:
        return a
    return numsun(a, b - 1)


a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
print(f'{a} + {b} = {numsun(a, b)}')
