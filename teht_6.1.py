import random
def di():
    dice = random.randint(1,6)
    return dice

while True:
    dice = di()
    print(dice)
    if dice == 6:
        break

