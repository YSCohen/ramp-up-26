import random

num = random.randint(1, 100)

if num < 50:
    print("You chose a number less than 50.")
elif num > 50:
    print("You chose a number more than 50.")
else:
    print("This behavior was not specified")
