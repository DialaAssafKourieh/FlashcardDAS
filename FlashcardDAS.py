'''🎴🎴🎴 Flashcard Program:
The user will receive a random set of seven (7)quiz questions using the Random_question module
from three categories: Biology, Geography, and History,which they can choose between.
After completing the quiz, the user will be asked whether the  want to move to another category
or end the quiz. Each time, the program will display the user’s score and the number of 
questions answered.'''

#🛬🐼Import Random_question module that choose the question from each category randomly
import Random_question as Rq
#🤷‍♀️Define new type of error called InvalidCategoryErro
class InvalidCategoryError(Exception):
#Define an empty block,Helps keep the code syntactically correct while you’re still developing.    
    pass

# define main function to ask the user and choose the category
def main():
    #assign numbers to each category
    Biology=1
    Geography=2
    History=3
    End=4
        
    # ask the user if he want to start quizz if not the program will be ended
    #the program will be repeatet every time the answer is y
    while True:
        #🧙ask the user if he want to play
        ques=input('Are you ready to play Flash Cards quizz 🎴 🎴 ? press 👍 Y or 👎 N :')
        
        #we check if ques = y ,using lower function to convert the letter to the lower case
        #it repeat asking question if ques was not in (y,n)
        while  ques.lower() not in ['y','n']:
               print ('Invalid input.Enter only Y 👍 or N 👎.')
               ques=input('Are you ready to play Flash Cards quizz? press 🎴🎴 Y or N :')
       
        if ques.lower() =='n' :     
           print ('Enjoy Your Life 🍺.') 
           break #Exit program
       #in case the answer was not 'n'
        print ('choose a categories or exit the game.')
        print ('1• 🧠  Biology')
        print ('2• 🏝️  Geography') 
        print ('3• 📗  History ')
        print ('4• 🙋  To Exit tap 4')
        
        #create a loop while the answer is y
        while True: 
              try:   
                    cat=int(input('🔢Choose the category (1-4) :')) 
                    if cat not in (1, 2, 3, 4) :
                        #raise an error in case the category is a number but not in the range 1--4
                        raise InvalidCategoryError("🔢Category must be between 1 and 4! ")
                    break 
              except ValueError:
                        print('Invalid input, you must entre a number from 1 to 4 🔢.')
              except InvalidCategoryError as e:
                            print(e)
        #we will handle the case cat is in (1,2,3,4)
        if  cat==1:
                sheetname = 'Biology'
                print('you have 7 question in biology 🧠')
                #🧠 call random_question for the sheetname Biology
                Rq.rand_ques(sheetname)
                
        elif cat==2:
                sheetname = 'Geography'
                print('you have 7 question in Geography 🏝️')
                #🏝️call random_question for the sheetname Geography
                Rq.rand_ques(sheetname)
                
        elif cat==3:
                sheetname = 'History1'
                print('you have 7 question in Histoy📗 ')
                #📗call random_question for the sheetname History
                Rq.rand_ques(sheetname)
                
        elif cat==4:
                #end the quizz
                print('Enjoy your life 🍺.')
                exit(0)
                      

if __name__=='__main__'  :
   main()      