# Disarium Number
# https://edabit.com/challenge/yvJbdkmKHvCNtcZy9


def is_disarium(n: int):
    as_str = str(n)
    total = sum(
        digit**place
        for place, digit in zip(range(1, len(as_str) + 1), (int(c) for c in as_str))
    )
    return total == n


if __name__ == "__main__":
    for n, r in zip(
        [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
        [True, False, True, False, False, True, True, False, False, True, True, True],
    ):
        assert is_disarium(n) == r
