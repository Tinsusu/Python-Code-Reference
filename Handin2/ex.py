'''necessary_var = "hello"
if (len(necessary_var) > 4):
    neccessary_var = necessary_var[:4]  # truncate if length larger than 4
print(necessary_var)'''


''' Functions with return values - Exercise
Change your die function so that it returns its result, instead of printing it
Create another function called dice that simulates throwing two dice and calculating the sum. 
This function should use the die function. Note how essential it is that the die function returns 
it's value instead of merely printing it.
'''
import random
def die():
  i = random.randint(1,6)
  return i

x = die()
print(x)

def sum():
  x1 = die()
  x2 = die()
  return x1 + x2

print(sum())


def cointoss(headprobability):
  rand_i = random.randint(0, 1)
  outcomes = ["Heads", "Tails"]
  return outcomes[rand_i]


def biasecoin(p):
    if random.random() < p:
        return "Heads"
    else:
        return "Tails"
biasecoin(0.6)

import random

def die():
    x = random.random
    return 1+int(x*6)

def dice():
    d1 = die()
    d2 = die()
    return d1+d2

print(dice())

