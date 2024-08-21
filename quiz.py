questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    {"question": "What is the largest living species of lizard?", "answer": "Komodo dragon"},
    {"question": "What is the deepest ocean?", "answer": "Pacific Ocean"}
]

def quiz_game():
    score = 0
    for question in questions:
        answer = input(question["question"] + " ")
        if answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is " + question["answer"])
    print("Your final score is " + str(score) + " out of " + str(len(questions)))

quiz_game()
