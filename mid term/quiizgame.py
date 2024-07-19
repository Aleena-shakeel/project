#project quiz game
print("****************")
print("WELCOME TO MY QUIZ GAME")
print("****************") 



questions = [
    { "question": "Who developed the python language?",
        "options": ["A) Dnnis Ritchie", "B) Guido van Rossum", "C) james gosling", "D) WIck van Rossum"],
        "answer": "B" },
    {"question": "In which year was the python language developed?",
        "options": ["A) 1989 ","B) 1999", "C) 1991", "D) 1998"],
        "answer": "A"},
    {"question": "In which language is python written?",
        "options": ["A) english", "B) php", "C) C", "D) All of above"],
        "answer": "C"},
    {"question": "Which character is used in python to make a single line comment?",
        "options": ["A) /", "B) //", "C) #", "D) !"],
        "answer": "C"},
    {"question": "Which one of the following is the correct extension of the phython file?",
        "options": ["A) .py", "B) .phython", "C) .p", "D) none of these"],
        "answer": "A"},
    {"question": "Which is incorrect variable name?",
        "options": ["A) Id_No", "B)ID_NO", "C) IdNo", "D) ID No"],
        "answer": "D"},
    {"question": "Which of the following is not a valid relational operator?",
        "options": ["A) =", "B) <", "C) >", "D) !"],
        "answer": "A"},
    {"question": "What is the answer to this expression ,22 % 3 is?",
        "options": ["A) 7", "B) 1", "C) 8", "D) 5"],
        "answer": "B"},
     {"question": "Which of the following is an valid variable?",
        "options": ["A) my_string_1", "B) 1st_string", "C) foo", "D) _"],
        "answer": "A"},
    {"question": "Which oneof the following is not a keyword in python language?",
        "options": ["A) true", "B) and", "C)swicth", "D) def"],
        "answer": "C"},  ]


# Function to run the quiz game
def run_quiz():
    score = 0
    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (ENTER A, B, C, or D): ").strip().lower()
        if answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("INCORRECT")
            print(f"{q["answer"]}.is the correct answer") 
    
    print(f"Your final score is: {score} out of {len(questions)}")


if __name__ == "__main__":
    run_quiz()
    print("Thanks for playing!")