# Valid Number Information
def valid_number_information():
    valid_numbers = []
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    for i in numbers:
        if i > 0 and i < 100:
            valid_numbers.append(i)
    valid_numbers_sum = sum(valid_numbers)
    valid_numbers_average = sum(valid_numbers) / len(valid_numbers)
    print(f"The valid numbers are: {valid_numbers}")
    print(f"The sum of the valid numbers is: {valid_numbers_sum}")
    print(f"The average of the valid numbers is: {round(valid_numbers_average, 2)}")
valid_number_information()

# Number Analysis Program
def number_analysis_program():
    count = 1
    number_list = []
    while count < 21:
        number = int(input(f"Enter number {count}: "))
        number_list.append(number)
        count += 1
    lowest_number = min(number_list)
    highest_number = max(number_list)
    number_total = sum(number_list)
    number_average = sum(number_list) / len(number_list)
    print(f"The number list is {number_list}")
    print(f"The lowest number in the list is {lowest_number}")
    print(f"The highest number in the list is {highest_number}")
    print(f"The total of the numbers in the list is {number_total}")
    print(f"The average of the numbers in the list is {number_average}")
number_analysis_program()