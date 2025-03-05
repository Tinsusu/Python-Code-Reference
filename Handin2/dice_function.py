import random

def die():
    x = random.random()
    return 1+int(x*6)

def dice():
    d1 = die()
    d2 = die()
    return d1+d2

print(dice())