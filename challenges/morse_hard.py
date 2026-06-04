# Encode Morse
# https://edabit.com/challenge/5bYXQfpyoithnQisa

char_to_dots = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": " ",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}

legal_chars = "".join(char_to_dots.keys())


def encode_morse(message: str):
    message = message.upper()

    if any((c not in legal_chars) for c in message):
        raise ValueError(f'All characters must be in "{legal_chars}"')

    return " ".join(char_to_dots[c] for c in message)


if __name__ == "__main__":
    assert (
        encode_morse("EDABBIT CHALLENGE")
        == ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
    )

    assert encode_morse("HELP ME !") == ".... . .-.. .--.   -- .   -.-.--"

    assert encode_morse("CHALLENGE") == "-.-. .... .- .-.. .-.. . -. --. ."

    assert (
        encode_morse(
            "1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."
        )
        == ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-"
    )

    assert (
        encode_morse("did you got my mail ?")
        == "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--.."
    )

    assert (
        encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C")
        == "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-."
    )

    print("All tests passed")
