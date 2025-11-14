#this module choose a random question from Excel file
#Flashcarddata1 sheet BIOLOGY
import pandas as pd
import random

def rand_ques():
    score=0
    for count in range(7):
      df = pd.read_excel('FlashcardsDAS.xlsx', sheet_name='Geography')
      #choose a random question , use sample avoiding repetition
      random_row = df.sample(n=1)
      random_ques = df.iloc[random_row, 0]
      random_answer = df.iloc[random_row, 1]
      print(random_ques)
      answer=input('Enter the Answer:')
      if answer.lower()==random_answer.lower():
        print('Correct answer.')
        count +=1
        print(f'{count}/7')
        score +=1
        print (f'The score is {score}')
      elif  answer.lower()!=random_answer:  
        print('Wrong Answer.')
        count+=1
        print(f'{count}/7')
if __name__=='__rand_ques__':
   rand_ques()

rand_ques() 
          #print(random_row)
    
    #print(random_answer)
    # random_ques = df.iloc[:, 0].sample(n=1).values[0]  # n=1 means 1 random row
    # print(random_ques)
    #return df.iloc[:, 0].sample(n=1)

