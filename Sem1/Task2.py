count_boats = int(input('Enter count boats: '))
petya = 0
kate = 0
sergey = 0
if (count_boats % 2 == 0 and count_boats > 5):
    if(count_boats % 3 == 0):
        kate = count_boats - (count_boats // 3)
        petya = kate // 4
        sergey = petya
        print(petya,kate,sergey)
    else:
        print("You can't make a half-ship!!")
else:
    print('Error! Enter an even number greater than 5!')