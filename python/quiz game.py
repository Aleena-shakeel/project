#PROJECT QUIZ GAME

questions = (("Plants growing in salt marshes are called?: "),
             ("How many bones in human body "),
             ("RBCs stands for?: "),
             ("Which element are called element of life?: "),
             ("Quaid-e-Azam was born in?:"),
            ("Type of immunity present in birth?: "),
             ("The formula for electric potential difference is?: "),
             ("Bggest animal in the world is?:"),
             ("This was awarded to bilquis edhi?:"),
             ("Which animal lays the largest eggs?: "),)

options = (("A. Hydrophytes","B. Halophytes","C. mesophytes","D. xerophytes" ),
           ("A. 306","B. 206","C. 208","D. 258"),
           ("A. White blood cells","B. Plasma","C. Red blood cells","D. Hemoglobin"),
           ("A. Hydrogen","B. Carbon","C. Oxygen","D. Nitrogen"),
           ("A. Lahore","B. Peshawar","C. Islamabad","D. Karachi"),
           ("A. Ative","B. passive","C. Innate","D. Adptive"),
           ("A. V=IR","B. V=I/R","C. V=R/I","D. I=VR"),
           ("A. Whale","B. Elephant","C. Sharke","D. Giraffe"),
           ("A. Hilal-e-imtiaz","B. Nishan-e-haider","C. Sitare jurat","D. Noble prize"),
           ("A. Eagle","B. Ostrich","C. Elephant","D. Owl"),)

answers =("B","B","C","B","D","C","A","A","A","B")
guesses =[]
score = 0
question_num = 0

for question_num in range(len(questions)):
    print("------------")
    print(questions[question_num])
    for i in options[question_num]:
     print(i)

guess = input("Enter(A,B,C,D): ").upper()
guesses.append(guesses)
if guess == answers[question_num]:
     score += 1
     print("CORRECT!")
else:
     print("INCORRECCT!")
     print(f"{answers[question_num]} is the correct answer")
     question_num += 1

print("-----------------")
print("      RESULT     ")
print("-----------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()    


print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()    

score = int(score / len(questions) * 100)
print(f"your score is :{score}%")