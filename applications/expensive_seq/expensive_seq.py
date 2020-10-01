# Your code here
cache = {} #empty dictionary for equations


def expensive_seq(x, y, z):
    # Your code here
    if (x, y, z) not in cache:  # not in cache
        if x <= 0:  # if x is less than 0
            # add to cache and add y + z
            cache[(x, y, z)] = y + z
        else:  # otherwise
            if x > 0:  # if x is greater than 0
                # add to cache and do equations
                cache[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
                    expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    # return the cache x y z
    return cache[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
