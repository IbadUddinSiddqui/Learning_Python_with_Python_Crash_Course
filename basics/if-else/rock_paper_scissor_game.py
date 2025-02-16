import random
from rich.console import Console
# Move these outside the loop since we want to track total score
user_points = 0
computer_points = 0
turns = 3
choices = ["rock", "paper", "scissors"]

while turns > 0:
    computer_choice = random.choice(choices)
    user_choice = str(input("Enter rock, paper or scissors.... or exit to exit the game ")).lower()
    
    # Add exit condition
    if user_choice == "exit":
        break
        
    # Validate input
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper or scissors")
        continue
    
    print(f"\nComputer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("Game Tied!")
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
          (user_choice == "scissors" and computer_choice == "paper") or 
          (user_choice == "paper" and computer_choice == "rock")):
        print("You Win!")
        user_points += 1
    else:
        print("You Lost!")
        computer_points += 1
    
    turns -= 1
    print(f"\nScore:\nYour Score: {user_points}\nComputer Score: {computer_points}\nRemaining Turns: {turns}\n")

# Show final results
print("\nGame Over!")
print(f"Final Score:\nYou: {user_points}\nComputer: {computer_points}")
if user_points > computer_points:
    print("Congratulations! You won the game!")
elif computer_points > user_points:
    print("Computer wins! Better luck next time!")
else:
    print("It's a tie!")
    
