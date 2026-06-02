import random


def Echo():
    nums = ""
    for _ in range(20):
        nums += f"{random.randint(0, 100)}\n"
    with open("theFile.txt", "w") as f:
        f.write(nums)
