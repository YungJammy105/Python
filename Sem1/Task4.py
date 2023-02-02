n = int(input('Enter length of chocolate: '))
m = int(input('enter width of chocolate: '))
k = int(input('Number of slices: '))

if (k % n == 0 or k % m == 0) and (k < m*n):
    print(f'Chocolate can be divided into {k} slices')
else:
    print("Chocolate can't be divided")