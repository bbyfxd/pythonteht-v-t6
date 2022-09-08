import random
def di(tahkot):
    number = random.randint(1,tahkot)
    return number

tak = int(input("How many?: "))
while True:
    dice = di(tak)
    print(dice)
    if dice == tak:
        break
