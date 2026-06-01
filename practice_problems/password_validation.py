while True:
    pswd = input("password: ")

    if len(pswd) < 8:
        print("Password must be at least 8 characters")
    elif not any(c.isdigit() for c in pswd):
        print("Password must contain a number")
    elif not any(c.islower() for c in pswd):
        print("Password must contain a lowercase letter")
    elif not any(c.isupper() for c in pswd):
        print("Password must contain an uppercase letter")
    elif not any(c in "!@#$%^&*()_+=-`~';:\"/?.>,<{}\\|[]" for c in pswd):
        print("Password must contain a special character")
    else:
        print(f"{pswd} is a valid password")
        break
