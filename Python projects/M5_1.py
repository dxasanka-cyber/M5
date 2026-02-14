import random
num_dice = int(input("How many dice would you like to roll?"))
total = 0
for i in range(num_dice):
    roll = random.randint(1,6)
    print("Dice",i + 1,"rolled",roll)
    total += roll
    print("Total sum is:",total)