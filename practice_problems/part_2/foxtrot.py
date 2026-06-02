def Foxtrot(number: float):
    return number * 2


if __name__ == "__main__":
    n = 1

    for i in range(11):
        print(f"2^{i} = {n}")
        n = Foxtrot(n)
