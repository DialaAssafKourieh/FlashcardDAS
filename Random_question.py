import pandas as pd
import random

def rand_ques(sheet_to_read='Biology'):
    # Load the Excel sheet once
    # sheet_to_read ="History1"
    df = pd.read_excel('FlashcardsDAS.xlsx', sheet_name=sheet_to_read)

    #sheet_name=['Biology','Geography','History1'])
    # Select 7 random rows without repetition
    random_rows = df.sample(n=7, replace=False)
    score = 0
    count = 0
#iterrows() function lets you loop over each row in the DataFrame.
    for index, row in random_rows.iterrows():
        question = row["Questions"]
        correct_answer = row["Answers"] 

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