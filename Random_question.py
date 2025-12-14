'''The module Random_question chooses the 
   random questions from the excel file FlaschcardDAS.xlsx. 
   We call it from the main program Rq.rand_ques(sheetname) where the sheetname
   refers to the chosen category '''

# panda is a python library that helps us to read the excel file
import pandas as pd

file_path=('FlashcardsDAS.xlsx')
# define the function that is called in the main program for the argument Biology
def rand_ques(sheet_to_read='Biology'):
   try:
       df = pd.read_excel('FlashcardsDAS.xlsx', sheet_name=sheet_to_read)

        # sheet_name=['Biology','Geography','History1'])
        # Select 7 random rows without repetition using the sample function.
    
       random_rows = df.sample(n=7, replace=False)
       score = 0
       count = 0

        # iterate over the rows of the excel file as (index, Series) pairs so that the row for questions corresonds with the row for answers

       for index, row in random_rows.iterrows():
            question = row["Questions"]
            correct_answer = row["Answers"] 

            # print the question
            print(f"\n Question {count+1}: {question}")

            # removes any extra white space at the start and end of the string.
            answer = input("Enter your answer: ").strip()

            # Case-insensitive comparison
            if answer.lower() == str(correct_answer).lower():
                    print("✅ Correct answer.")
                    score += 1
            else:
                    print(f"❌ Wrong answer. The correct answer is: {correct_answer}")

            count += 1
            print(f"Progress: {count}/7 | Current Score: {score}")

            print(f"\nQuiz completed! Your final score is {score}/7.")
   except FileNotFoundError:
       print('Error The File Flashcards.xlsx is not found. Make sure the file exists.')        
       return
# Run the quiz
if __name__ == '__main__':
    rand_ques()