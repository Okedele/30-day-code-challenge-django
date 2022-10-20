# RANDOM NUMBER FILE WRITER
import random

def random_number_file_writer():
    no_of_random_numbers = int(
        input("Specify how many random numbers the file will hold: ")
    )
    for i in range(no_of_random_numbers):
        random_number = random.randint(1, 500)
        file = open("randomNumberFile", "a")
        file.write(f'{random_number}\n')
        file.close()
    print("Process completed......")

random_number_file_writer()
