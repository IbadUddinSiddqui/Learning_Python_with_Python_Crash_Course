import random
import time

# Game setup
user_points = 0
computer_points = 0
turns = 3
choices = ["rock", "paper", "scissors"]
choice_emojis = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Game header
print("\n" + "="*50)
print("🎮 ROCK PAPER SCISSORS GAME 🎮".center(50))
print("="*50 + "\n")

while turns > 0:
    # Show remaining turns
    print(f"\n🎯 Round {4-turns} of 3")
    print("-"*50)
    
    computer_choice = random.choice(choices)
    user_choice = str(input(f"🎮 Your turn! Enter rock {choice_emojis['rock']}, paper {choice_emojis['paper']} or scissors {choice_emojis['scissors']}... \n(or type 'exit' to quit): ")).lower()
    
    # Add exit condition
    if user_choice == "exit":
        print("\n👋 Thanks for playing!")
        break
        
    # Validate input
    if user_choice not in choices:
        print("\n❌ Invalid choice! Please try again!")
        continue
    
    # Build suspense
    print("\nRock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot!\n")
    time.sleep(0.3)
    print(f"🎮 You chose: {user_choice.upper()} {choice_emojis[user_choice]}")
    print(f"🤖 Computer chose: {computer_choice.upper()} {choice_emojis[computer_choice]}")
    
    if user_choice == computer_choice:
        print("\n🤝 Game Tied!")
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
          (user_choice == "scissors" and computer_choice == "paper") or 
          (user_choice == "paper" and computer_choice == "rock")):
        print("\n🎉 You Win!")
        user_points += 1
    else:
        print("\n💔 You Lost!")
        computer_points += 1
    
    turns -= 1
    print("\n📊 SCOREBOARD")
    print("-"*20)
    print(f"🎮 You: {user_points}")
    print(f"🤖 Computer: {computer_points}")
    print(f"🎯 Remaining Turns: {turns}")

# Show final results
print("\n" + "="*50)
print("🏁 GAME OVER 🏁".center(50))
print("="*50)
print("\n🏆 FINAL SCORE:")
print("-"*20)
print(f"🎮 You: {user_points}")
print(f"🤖 Computer: {computer_points}\n")

if user_points > computer_points:
    print("🎉 Congratulations! You won the game! 🏆")
elif computer_points > user_points:
    print("🤖 Computer wins! Better luck next time! 🎲")
else:
    print("🤝 It's a tie! Well played! 🎮")

print("\n" + "="*50)