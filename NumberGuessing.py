import random

while True:
    actualNumber = random.randint(1, 100)

    print("Welcome to Number Guessing Game")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ")

    if difficulty == 'easy':
        counter = 10
    else:
        counter = 5

    while counter > 0:
        print(f"You Have {counter} attempts remaining.")
        num = int(input("Make a guess: "))
        if num == actualNumber:
            print("Congratulations. Correct Guess. ")
            break
        elif num < actualNumber:
            counter -= 1
            print("Too low.")
            if counter != 0:
                print("Guess Again.")
        else:
            counter -= 1
            print("Too high.")
            if counter != 0:
                print("Guess Again.")

    if counter == 0:
        print("You Lost. Better luck next time")

    while True:
        again = str(input('Run again? (y/n): '))
        if again in ('y', 'n'):
            break
        print("Invalid input.")
    if again == 'y':
        continue
    else:
        print("Goodbye.")
        break
