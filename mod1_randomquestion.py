#this module choose a random question from Excel file
#Flashcarddata1 sheet BIOLOGY
import pandas as pd
import random

def rand_ques():
    df = pd.read_excel('Flashcardsdata1.xlsx', sheet_name='BIOLOGY')
    
    random_row = random.randint(0, df.shape[0])

    random_ques = df.iloc[random_row, 0]
    random_answer = df.iloc[random_row, 1]

    print(random_row)
    print(random_ques)
    print(random_answer)
    # random_ques = df.iloc[:, 0].sample(n=1).values[0]  # n=1 means 1 random row
    # print(random_ques)
    #return df.iloc[:, 0].sample(n=1)
rand_ques()


########
#hier I shoul know how to return the row number 
# to use it in the answer mod2_cmp_answer
 