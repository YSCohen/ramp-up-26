from math import sqrt


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True

print(" | ".join(str(i) for i in range(100, 1000) if isprime(i)))
