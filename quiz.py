def new_game():
    guessess = []
    correct_guessess = 0
    question_number = 1

    for key in questions:
        print("-----------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess = input("Enter A, B, C, or D: ")
        guess = guess.upper()
        guessess.append(guess)

        correct_guessess += check_answer(questions.get(key), guess)

        question_number += 1

    display_score(correct_guessess, guessess)

def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!!")
        return 0
    
def display_score(correct_guessess, guessess):
    print("<------------------------------>")
    print("             Result             ")
    print("<------------------------------>")

    print("Answers = ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guessess = ", end="")
    for i in guessess:
        print(i, end=" ")
    print()

    score = int((correct_guessess/len(questions))*100)
    print("Your score is "+str(score)+"%")

def play_again():
    response = input("Do you want to play again? (Yes/No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False 

questions = {
    "Is the earth round?: ":"A",
    "Which car brand is the best?: ":"C",
    "Who is the president of Indonesia?: ": "B",
    "What is the capital of Japan?: ":"D"
}

options = [["A. Yes", "B. No", "C. I don't know", "D. Earth???"],
           ["A. Toyota", "B. BMW", "C. Porshe", "D. Mercedes"],
           ["A. Megawati", "B. Jokowi", "C. Obama", "D. Saddam Husein"],
           ["A. Beijing", "B. Jakarta   ", "C. Rome", "D. Tokyo"]]

new_game()

while play_again():
    new_game()

print("BYE!")