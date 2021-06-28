"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def not_number_rejector(message):
    while True:
        try:
            number = int(input(message))
            print(f"{number} Looks good!")
            return number
        except Exception as general_error:
            print(f"This isn't a number. Try again!, {general_error}")


def super_asker(low, high):
    message = f"Give me a number between {low}, and {high}: "
    while True:
        try:
            number = int(input(message))
            if low < number < high:
                print(f"{number} Looks good!")
                return number
            else:
                print(f"{number} isn't between {low}, and {high}: ")
        except Exception as general_error:
            print(f"This isn't a number. Try again!, {general_error}")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    low = not_number_rejector("Enter a lower bound: ")
    high = super_asker(low, float("infinity"))
    print(f"OK then, a number between {low} and {high} ?")

    actualNumber = random.randint(low, high)

    guessed = False

    while not guessed:
        guessed_number = not_number_rejector("Guess a number: ")
        print(f"You guessed {guessed_number}")
        if guessed_number == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
        elif low < guessed_number < actualNumber:
            print("Too small, try again :'(")
        elif high > guessed_number > actualNumber:
            print("Too big, try again :'(")
        else:
            print(f"Not between {low} and {high} , try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
