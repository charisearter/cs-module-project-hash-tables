# Your code here
import math
import random

cache = {}  # empty dictionary to hold cache of numbers already factored


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
# make a memomization function to do slowfun or make slowfun the memomization ???
    if (x, y) not in cache:  # if x,y value are not in the cache
        # do the calculations for the new numbers
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        # add the values to the cache
        cache[x, y] = v
        # return the values x,y in the cache
    return cache[(x, y)]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
