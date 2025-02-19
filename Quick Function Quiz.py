QuestionStore = [
    'What is the capital of Canada? [A] Toronto, [B] Vancouver, [C] Ottawa, [D] Montreal',
    'Which continent is the driest on Earth? [A] Africa, [B] Antarctica, [C] Australia, [D] South America',
    'What is the longest river in the world? [A] Amazon River, [B] Mississippi River, [C] Yangtze River, [D] Nile River',
    'Which country has the most natural lakes? [A] Russia, [B] Canada, [C] Brazil, [D] United States',
    'Mount Everest is located on the border of which two countries? [A] Nepal and India, [B] China and Bhutan, [C] Nepal and China, [D] India and Pakistan'
]
AnswerStore = ['C', 'B', 'D', 'B', 'C']

def Quizmaster():#This Reads the question index, prints the first question, asks for an answer, if the answer is inline with the correct answer index then grants a point.
    Score = 0
    for i in range(len(QuestionStore)): #Print the first question, followed by the next questions until it runs out of questions
        print(QuestionStore[i])
        GoodAnswer = False  #Set the while error detection var to false
        while GoodAnswer == False:
            inputt = input().strip().upper() #Aquire input answer
            if inputt == AnswerStore[i].upper(): #If the answer is the same return correct
                Score += 1
                print(f'Correct! current score = {Score}')
                GoodAnswer = True     #Exit error detection
            elif inputt == ("A" or "B" or "C" or "D"):  #If answer is incorrect, but one of the options, return incorrect
                print('Incorrect, Sorry.')
                GoodAnswer = True       #exit error detection
            else:
                print("Invalid Answer, Try Again") #answer wasn't in the list or correct, try answer again.
    print()
    print()
    print(f'Your final score was {Score}!')  #Ran out of questions
    
while True:
    Quizmaster()  #Run quizmaster
    if input("X to exit      ").upper() == "X": #If x is inputted quit
        quit()
