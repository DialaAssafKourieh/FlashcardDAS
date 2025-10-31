#Flash card main program ,use mod1_randomquesion to get the 
#random question, and mod2_cmp_answer to get the answer
#and Flashcardsdata.xlsx excel data file
####### F
import mod1_randomquestion
#choose the The Categories
BIOLOGY=1
GEOGRAPHY=2
HISTORY=3
EXIT=4
#the main function
def main():
    #define a choose variable control the loop
    #and hold the user menue
    choice=0
    while choice!=EXIT:
        #display the ctagories
        display_cat()
        #Get the user choice
        choice =int(input('Enter the category: '))
        #perform the selected action
        if choice ==BIOLOGY:
            print('Answer the folowing answers:')
            print (mod1_randomquestion.rand_ques())
            answer =str(input('Enter the answer: '))
             #write the module to compare the answer with typed answer
        
        elif choice ==GEOGRAPHY:
            print('Answer the folowing answers:')
            print (mod1_randomquestion.rand_ques())
            answer =str(input('Enter the answer: '))
              #write the module to compare the answer with typed answer
              #we should compare the entered answer with the one from th module function

        
        elif choice== HISTORY:
            print('Answer the folowing answers:')
            print (mod1_randomquestion.rand_ques())
            answer =str(input('Enter the answer: '))
            #write the module to compare the answer with typed answer
        elif choice==EXIT:
            print('Exit the game')
        else:
            print('Invalid category number')
       
#function that display all the ctagories
def display_cat():
    print('Ctegories')
    print('1- Biology')
    print('2- Geography')
    print('3- History')
    print('4- Exit')
main()    

        
    

