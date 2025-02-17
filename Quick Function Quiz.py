QuestionStore = [
    'What is the capital of Canada? [A] Toronto, [B] Vancouver, [C] Ottawa, [D] Montreal',
    'Which continent is the driest on Earth? [A] Africa, [B] Antarctica, [C] Australia, [D] South America',
    'What is the longest river in the world? [A] Amazon River, [B] Mississippi River, [C] Yangtze River, [D] Nile River',
    'Which country has the most natural lakes? [A] Russia, [B] Canada, [C] Brazil, [D] United States',
    'Mount Everest is located on the border of which two countries? [A] Nepal and India, [B] China and Bhutan, [C] Nepal and China, [D] India and Pakistan'
]
AnswerStore = ['C', 'B', 'D', 'B', 'C']

def Quizmaster():
    Score = 0
    for i in range(len(QuestionStore)):
        print(QuestionStore[i])
        
        try:
            if input().strip().upper() == AnswerStore[i].upper():
                Score += 1
                print(f'Correct! current score = {Score}')
                
            else: print('Incorrect, Sorry.')
            
        except:
            print("Invalid Answer")

    print()
    print()
    print(f'Your final score was {Score}!')
    


    
Quizmaster()
