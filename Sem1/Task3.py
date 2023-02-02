number_ticket = int(input())
first_half = number_ticket // 1000
second_half = number_ticket % 1000
first_sum = 0
second_sum = 0
print(number_ticket,first_half,second_half)
while first_half > 0:
    x = first_half % 10
    y = second_half % 10
    first_sum += x
    second_sum += y
    first_half //= 10
    second_half //= 10
if (first_sum == second_sum):
    print(f'Your ticket №{number_ticket} lucky')
else:
    print(f'Your ticket №{number_ticket} is unlucky')