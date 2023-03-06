firstElement, step, n = (map(int, input().split()))
list1 = []

for i in range(1, n + 1):
    list1.append(firstElement + ((i-1) * step))
print(list1)
