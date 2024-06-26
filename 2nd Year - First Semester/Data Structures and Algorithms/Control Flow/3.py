from random import randint

flag = True

while flag != False:

    random_number = randint(1,2)
    guess = 0

    print("\nI have a number between 1-50"
        "\nCan you guess my number?"
        "\nPlease type your first guess\n")

    while guess != random_number:
        guess = int(input("Guess: "))

        if (guess > random_number):
            print("Too High. Try again.")
        elif (guess < random_number):
            print("Too Low. Try again.")
        else:
            print("Excellent! You guessed the number!")

    answer = input("Would you like to play again? (y or n)")

    if answer.lower() == 'y':
        continue
    else:
        break