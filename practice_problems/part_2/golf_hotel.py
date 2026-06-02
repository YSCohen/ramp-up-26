import random


def Golf():
    return random.randint(1, 6)


def Hotel():
    i = 0
    a = 0
    b = 1
    while a != b:
        i += 1
        a = Golf()
        b = Golf()
    print(f"getting equal dice rolls took {i} attempts")
