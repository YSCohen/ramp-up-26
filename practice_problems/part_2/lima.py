def Lima(data: dict):
    data["name"] = input("name: ")

    for _ in range(3):
        entered_age = int(input("age: "))
        if 0 <= entered_age <= 100:
            data["age"] = entered_age
            return

    data["age"] = 0
