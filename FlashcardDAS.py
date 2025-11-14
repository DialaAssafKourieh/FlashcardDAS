#n this program, the user will receive a random set of seven (7) quiz questions from three categories:
#  Biology, Geography, and History. The user can choose a category, 
# and after completing the quiz, the score will be recorded in an output file.
#After each quiz, the user will be asked whether they want to move to another category or end the quiz. Each time, 
# the program will display the user’s score and the number of questions answered.
####Diala
import Random_question as Rq
def main():
    Biology=1
    Geography=2
    History=3
    End=4
    # ask the user if he want to start quizz if not the program will be ended
    ques=input('Are you ready to play Flash Cards quizz? press  Y or N :')
    if ques.lower() == 'y':
        print ('You have to choose one of the categories or end the game.')
        print ('For Biology tap 1')
        print ('For Geography tap 2')
        print ('For History tap 3')
        print ('To Exit tap 4')
        #handle the error
        cat=int(input('Choose the category :'))
        #we should discuss each category
        if cat==1:
            print('you have 7 question in biology')
            Rq.rand_ques()
        #category is Biology we should ask him 7 random questions
        #  and show the score after each question
        elif cat==2:
             print('you have 7 question in Geography')
        #category is Geography we should ask him 7 random questions
        #  and show the score after each question
        elif cat==3:
             print('you have 7 question in Histoy')
        #category is Histoy we should ask him 7 random questions
        #  and show the score after each question
        elif cat==4:
            #end the quizz
            pass
        else :
            cat=int(input('Enter a valid number'))
            #we should repeat again ???????

        #Complete
    elif ques.lower() == 'n':
        print('Enjoy your life.')
        pass
    else:
        print('You can entre only Y or N ')
        ques=input('Are you ready to play Flash Cards quizz? press  Y or N :')
        #go to the begining
if __name__=='__main__'  :
   main()      