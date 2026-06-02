def Kilo(nums: list[int]):
    halves = ""
    for i in nums:
        halves += f"{i / 2}\n"
    with open("theFile.txt", "w") as f:
        f.write(halves)
