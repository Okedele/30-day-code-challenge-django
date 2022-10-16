# SLEEP DEBT
total_sleep_hours = 0
expected_sleep_hours = 7 * 8
for i in range(1, 8):
    sleep_hours = int(input(f"How many hours do you sleep on day {i}?: "))
    total_sleep_hours += sleep_hours
sleep_debt = expected_sleep_hours - total_sleep_hours
if (sleep_debt > 0):
    print(f"You have a sleep debt of {sleep_debt} hours")
else:
    print(f"You do not have a sleep debt. You don't know how lucky you are. I am soooooo jealous.")

# POPULATION
organism_starting_number = int(input("Starting number of organisms: "))
average_population_increase = float(input("Average daily increase (percentage): "))
multiplication_days = int(input("Number of days to multiply: "))
population = 0

print("Day\t\tPopulation")

for i in range(1, multiplication_days+1):
    if (i == 1):
        population = organism_starting_number
    else:
        population += average_population_increase / 100 * population
    print(f"{i}\t\t{population}")