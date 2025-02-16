# Dictionary to store questions and answers
quiz_questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "What is 2 + 2?": "4",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the largest mammal in the world?": "blue whale"
}

def play_quiz():
    score = 0
    total_questions = len(quiz_questions)
    
    print("Welcome to the Quiz Game!")
    print(f"There are {total_questions} questions. Let's begin!\n")
    
    # Iterate through questions and answers
    for question, correct_answer in quiz_questions.items():
        # Display question and get user's answer
        print(question)
        user_answer = input("Your answer: ").lower().strip()
        
        # Check if answer is correct
        if user_answer == correct_answer:
            print("Correct! ✅")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was: {correct_answer}")
        print()  # Empty line for better readability
    
    # Display final score
    print(f"Quiz completed! Your score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage}%")

# Start the game
if __name__ == "__main__":
    play_quiz()
