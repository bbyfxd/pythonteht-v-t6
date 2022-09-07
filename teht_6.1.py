import random

min, max = 1, 6

while True:
    r = random.randint(min, max)
    print(r)
    if r == 6:
        break
