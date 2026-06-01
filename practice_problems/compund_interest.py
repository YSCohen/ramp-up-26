principal = float(input("principal: "))
interest_rate = float(input("interest rate: "))
years = float(input("years: "))

amount = principal * (1 + interest_rate) ** years

print(amount)
