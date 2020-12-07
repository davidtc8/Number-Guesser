import art
import random

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 0 and 30...")

decision = input("Choose a difficulty between 'Easy', 'Medium' and 'Hard': ").lower()

def hard():
    """
    This function will run when the user chooses 'hard' in the game!
    The player will only have 5 lives.
    """
    lives = 5
    number = random.randint(0, 30)
    print("You have 5 attemps remaining to guess the number")
    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess > number and lives >= 1:
            print("Too high")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess < number and lives >= 1:
            print("Too low")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess == number:
            print('You win!')
            break

def medium():
    """
    This function will run when the user chooses 'medium' in the game!
    The player will only have 7 lives.
    """
    lives = 7
    number = random.randint(0, 30)
    print("You have 7 attemps remaining to guess the number")
    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess > number and lives >= 1:
            print("Too high")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess < number and lives >= 1:
            print("Too low")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess == number:
            print('You win!')
            break

def easy():
    """
    This function will run when the user chooses 'easy' in the game!
    The player will only have 10 lives.
    """
    lives = 10
    number = random.randint(0, 30)
    print("You have 10 attemps remaining to guess the number")
    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess > number and lives >= 1:
            print("Too high")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess < number and lives >= 1:
            print("Too low")
            lives -= 1
            print(f"You have {lives} attempts remaining ):")
            if lives >= 1:
                print('Guess again')
            else:
                print('You loose!')
        elif guess == number:
            print('You win!')
            break

if decision == 'hard':
    hard()
elif decision == 'easy':
    easy()
elif decision == 'medium':
    medium()
else:
    print(f"ayñ, Idk what you meant by {decision}")
