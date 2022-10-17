# Random Number Guessing Game
import random
def random_number_guess():
    random_number = random.randint(1, 100)
    guesses = 1
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the random number: "))
        if (guess < random_number):
            print("Too low, try again.")
        elif (guess > random_number):
            print("Too high, try again.")
        elif (guess == random_number):
            print(f"Congratulations!!!!!\nNumber of guesses: {guesses}\n\nGenerating new number.....\n")
            random_number = random.randint(1, 100)
            guesses = 0
            guess = 0
        guesses += 1

# Rock, Paper, Scissors Game
def hand(number):
    if (number == 1):
        return "rock"
    elif (number == 2):
        return "paper"
    elif(number == 3):
        return "scissors"

def rock_paper_scissors():
    random_number = random.randint(1, 3)
    computer_hand = hand(random_number)
    user_hand = input("Enter your choice: ").lower()
    print(f"Computer's choice: {computer_hand}\n")
    while computer_hand == user_hand:
        random_number = random.randint(1, 3)
        user_hand = input("Enter your choice: ").lower()
        computer_hand = hand(random_number)
        print(f"Computer's choice: {computer_hand}\n")
    if (computer_hand == "rock"):
        if (user_hand == "scissors"):
            print("Computer wins")
        else:
            print("User wins")
    if (computer_hand == "paper"):
        if (user_hand == "rock"):
            print("Computer wins")
        else:
            print("User wins")
    if (computer_hand == "scissors"):
        if (user_hand == "paper"):
            print("Computer wins")
        else:
            print("User wins")

            
rock_paper_scissors()
random_number_guess()