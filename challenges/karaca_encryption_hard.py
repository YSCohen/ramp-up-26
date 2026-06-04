vowel_subs = {
    "a": "0",
    "e": "1",
    "i": "2",
    "o": "2",
    "u": "3",
}


def encrypt(message: str):
    message = message[::-1]
    message = "".join(vowel_subs.get(c, c) for c in message)
    message += "aca"
    return message


if __name__ == "__main__":
    assert encrypt("karaca") == "0c0r0kaca"
    assert encrypt("burak") == "k0r3baca"
    assert encrypt("banana") == "0n0n0baca"
    assert encrypt("alpaca") == "0c0pl0aca"
    assert encrypt("hello") == "2ll1haca"
