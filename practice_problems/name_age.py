for i in range(3):
    name = input("name: ")
    age = input("age: ")

    if name.isalpha() and age.isdecimal() and int(age) >= 1 and int(age) <= 100:
        print("Acceptable")
        break
else:
    print("Unacceptable")
