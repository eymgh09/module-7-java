
def quiz_game():   # defining a quiz game fonction

    guesses = []  # list is = to guesses
    correct_guesses = 0 # declaring a variable name correct guesses = to cero
    question_num = 1  # current quiestion = to one
    
    for key in questions:   # a for loop declarin a question
        print("-------------------------")
        print(key)
        for alternative in options[question_num-1]: # nested for loop
            print(alternative)
        guess = input("Enter (A,B,C,D,E,F,or G): ")  # alternatives input
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answers(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)   
def check_answers(answers, guess):  # definnig a function to check the answers
    if answers == guess:
        print("Correct!")
        return 1
    else:                   # if and else statement (decision)
        print("Wrong")
    return 0
                    # defining a funtion to display the score
def display_score(correct_guesses, guesses):
    print("------------------------------")
    print("Results")
    print("------------------------------") # this lines separate the questions
    print("answers: ", end=" ")
    for currentQuestion in questions: # this for loop display the values fron the answers
      print(questions.get(currentQuestion), end=" ")
    print()
    print("guesses: ", end=" ")
    for currentQuestion in questions: # this will display the guesses
        print(questions.get(currentQuestion), end=" ") 
    print()

    print("guesses: ", end=" ")
    for current in guesses:
        print(current,end=" ")
        print()

    score = int((correct_guesses/len(questions))*100)# 
    print("your score is:"+str(score)+"%") # string concatination, this will print the score
    thePaintings = open ("paintings.txt","a") # writing to a file
    thePaintings.write ("the last scrore wast as fallow "+ str(score)+"\n")
    
def play_again():      # defining a function to play again
    response = input("Would you like to play one more time? (yes or no): ")
    response = response.lower()

    if response == "yes": # if else stetment to check the response yes or no
        return True
    else:
        return False

   # dicionary showing the questions plus the right enswer
questions = {
    "Starry Night is a master piece done by?: ": "B",    
    "during what period was The Kiss painted?: ": "G",
    "what movement dose the Three Musicians represents to?: ": "A",
    "what medium was apply to paint the Girl With a pearl Earrings?: ": "E",
    "Guernica was painted by Picasso and it refers to?: ": "C",
    "What year was The Scream painted, and for who?: ": "D",
    "who paint The Gioconda?: ": "F",
   
}
    # tuple list to show the posible answers
options = [["A. Rafael", "B. Van Gogh", "C. Monet", "D. Josefine", "E. Klint", "F. Da Vinci"],
           ["A. Bronce period", "B. Abstraction period", "C. Cubism", "D. Blue period", " E. Velasco", "F. Red period", "G. Golden period"],
           ["A. cubism", "B. Expressionism", "C. Moder Art", "D. Dada", "E. Realism", "F. Pop Art"],
           ["A. Acrylics", "B. Pollock", "C. Pastels", "D. Josefine", "E. Oil colors", "F. Da Vinci"],
          ["A. Drama", "B. Love", "C. War", "D. Dead", "E. Power", "F. peace"],
          ["A. Klint", "B. Dali-1995", "C. Monet", "D. Munch-1983", "E. Velasco", "F. Da Vinci"],
          ["A. Picasso", "B. Pollock", "C. Monet", "D. Josefine", "E. Modigliani", "F. Da Vinci"]]
    

quiz_game()
#print( play_again())     
while play_again(): # this while loop will ask if player will continue playing or not
    quiz_game()
        

print("thanks for playing my game")
print("maybe next time!") # reading a file
myPaintingsList = open ("paintings.txt" , "r")
theLine = myPaintingsList.readline() 

while theLine != "":
    print (theLine)
    theLine = myPaintingsList.readline()


