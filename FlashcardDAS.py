'''🎴🎴🎴 Flashcard Program:
The user will receive a random set of seven (7) quiz questions using the Random_question module
from three categories: Biology, Geography, and History which they can choose from.
After completing the quiz, the user will be asked whether they want to move to another category
or end the quiz. Each time the program will display the user’s score and the number of 
questions answered.'''

# 🛬Import Random_question module which chooses the questions randomly from each category
import Random_question as Rq
# 🤷‍♀️Defines new type of error called InvalidCategoryError
class InvalidCategoryError(Exception):
# Defines an empty block, helps keep the code syntactically correct while you’re still developing.
    pass

# define main function to ask the user and choose the category
def main():
    # assign numbers to each category
    Biology=1
    Geography=2
    History=3
    End=4
        
    # ask the user if he want to start the quiz, if not the program will be terminated
    # the program will be repeated every time the answer is y
    while True:
        # 🧙ask the user if he wants to play
        ques=input('Are you ready to play the Flashcards quiz ? Enter 👍 Y or 👎 N :')
        
        # check if ques = y using lower function to make it lowercase
        # ask for input again if ques was not in (y,n)
        while  ques.lower() not in ['y','n']:
               print ('Invalid input. Enter only Y 👍 or N 👎')
               ques=input('Are you ready to play the Flashcards quiz? Enter 👍 Y or 👎 N :')
       
        if ques.lower() =='n' :     
           print ('Enjoy Your Life 🍺.') 
           break # Exit program
       # In case the answer was not 'n'
        print ('Choose a category or exit the game.')
        print ('1• 🧠  Biology')
        print ('2• 🏝️  Geography')
        print ('3• 📗  History')
        print ('4• 🙋  To Exit')
        
        # create a loop that runs while the answer is y
        
        while True: 
              try:   
                    cat=int(input('🔢Choose a category (1-4) :')) 
                    if cat not in (1, 2, 3, 4) :
                        # raise an error in case the category is a number but not in the range 1-4
                       raise InvalidCategoryError("🔢Category must be between 1 and 4.")
                       #print("🔢Category must be between 1 and 4!")
                    break 
              except ValueError:
                        print('Invalid input, you must enter a number from 1 to 4 🔢.')
              except InvalidCategoryError as e:
                            print(e)
        #  handles the case when cat is 1, 2, 3 or 4
        if  cat==1:
                sheetname = 'Biology'
                print('You have 7 questions in Biology 🧠')
                #🧠 call random_question for Biology
                Rq.rand_ques(sheetname)
                
        elif cat==2:
                sheetname = 'Geography'
                print('You have 7 questions in Geography 🏝️')
                #🏝️call random_question for Geography
                Rq.rand_ques(sheetname)
                
        elif cat==3:
                sheetname = 'History1'
                print('You have 7 questions in History 📗')
                #📗call random_question for History
                Rq.rand_ques(sheetname)
                
        elif cat==4:
                # end the quiz
                print('Enjoy your life 🍺.')
                exit(0)
                      

if __name__=='__main__'  :
   main()      