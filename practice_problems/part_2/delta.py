def Delta():
    while True:
        age_str = input("age: ")
        if age_str.isdigit():
            age = int(age_str)
            if age >= 0 and age <= 100:
                return age


if __name__ == "__main__":
    print(f"Your age is {Delta()}")
