import random

while True:
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    correct_answer = num1 * num2

    while True:
        user_answer = input(f"How much is {num1} times {num2}? ")

        if user_answer.isdigit():
            user_answer = int(user_answer)

            if user_answer == correct_answer:
                print("Very good!")
                break
            else:
                print("No. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

    another_question = input("Do you want to try another question? (yes/no): ")
    if another_question.lower() != "yes":
        print("Goodbye!")
        break