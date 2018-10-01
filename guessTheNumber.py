import random
numberOfGuesses = 0
number = random.randrange(1, 101)
guess = input("Guess an integer between 1 and 100: ")
guess = int(guess)

while number != guess:
    if guess < number:
        numberOfGuesses += 1
        print("You have made " + str(numberOfGuesses) + " guesses.")
        guess = input("Guess an integer higher than your previous guess: ")
        guess = int(guess)
    elif guess > number:
        numberOfGuesses += 1
        print("You have made " + str(numberOfGuesses) + " guesses.")
        guess = input("Guess an integer lower than your previous guess: ")
        guess = int(guess)

if guess == number:
    numberOfGuesses += 1
    print("Congrats, you guessed the number! It took " + str(numberOfGuesses) + " tries to guess the number.")
