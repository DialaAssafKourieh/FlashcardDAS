'''The modoul Random_question is a module that choose the 
   random question from excel file FlaschcardDAS.xlsx. 
   we call it from the main program  Rq.rand_ques(sheetname) where sheetname 
   in excel file that contains the category'''

#panda helps to handle data
import pandas as pd
import random
import os
file_path=('FlashcardsDAS.xlsx')
#define the function that is called from the main program for the argument Biology
def rand_ques(sheet_to_read='Biology'):
   try:
     if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        # Load the Excel sheet once
        #function read_excel from panda can read the sheet that is assigned in shee_to_read
   except:
          df = pd.read_excel('FlashcardsDAS.xlsx', sheet_name=sheet_to_read)

        #sheet_name=['Biology','Geography','History1'])
        # Select 7 random rows without repetition using sample function repace =falce not to repeat
          random_rows = df.sample(n=7, replace=False)
          score = 0
          count = 0

        #iterate over the rows of a DataFrame as (index, Series) pairs

          for index, row in random_rows.iterrows():
            question = row["Questions"]
            correct_answer = row["Answers"] 

            #print the question
            print(f"\n Question {count+1}: {question}")

            #removes any extra whitespace at the start and end of the string.
            answer = input("Enter your answer: ").strip()

            # Case-insensitive comparison
            if answer.lower() == str(correct_answer).lower():
                # get emoji by precing windows plus .
                    print("✅ Correct answer.")
                    score += 1
            else:
                    print(f"❌ Wrong answer. The correct answer is: {correct_answer}")

            count += 1
            print(f"Progress: {count}/7 | Current Score: {score}")

          print(f"\nQuiz completed! Your final score is {score}/7.")

# Run the quiz
if __name__ == '__main__':
    rand_ques()