def mathpow(a, b):
    if b == 1:
        return a
    return a * mathpow(a, b - 1)


num = int(input('Enter number: '))
degree = int(input('Enter degree: '))

print(f'{num} in degree {degree} equals {mathpow(num, degree)}')
