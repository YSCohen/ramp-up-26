color = input("what is your favorite color? ")

match color:
    case "blue":
        print("Great choice.")
    case "red":
        print("Poor choice.")
    case "green":
        print("Not a bad choice.")
    case _:
        print("Sorry, that's not a primary color.")
