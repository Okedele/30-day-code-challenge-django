import math
principal = float(input("Principal amount: "))
interest_rate = int(input("Interest rate: "))
compounding_period = int(input("Compounding period: "))
time = int(input("No of years: "))

compound_interest = principal * math.pow(1 + (interest_rate / 100) / compounding_period, (compounding_period * time))

print("Amount in the account after", str(time), "years is", round(compound_interest, 2))