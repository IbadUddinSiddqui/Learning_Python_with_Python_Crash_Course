import random

secret_number = random.randint(1,100)
attempts = 0

guess_number = int(input("Enter a number: "))
attempts += 1

while guess_number != secret_number:
    if attempts >= 5:  # Check attempts limit first
        print("You have reached the maximum number of attempts")
        print(f'The secret number was {secret_number}')
        break
    elif guess_number > secret_number:
        print(f'The guessed number is too high, you have {5-attempts} attempts left')
    elif guess_number < secret_number:
        print(f'The guessed number is too low, you have {5-attempts} attempts left')
    
    guess_number = int(input("Enter a number: "))
    attempts += 1

if guess_number == secret_number:  # Add this check outside the loop
    print(f'You guessed the number correctly in {attempts} attempts!')