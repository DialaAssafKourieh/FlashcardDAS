#we will find the cooect answer that related to the random
#question
import pandas as pd
df = pd.read_excel('Flashcardsdata1.xlsx', sheet_name='BIOLOGY')
for i in range(2):
    random_row = df.sample(n=1)
    q = random_row['Questions'].values[0]
    a = random_row['Answers'].values[0]
    print(q)
    print(a)
    #print(f"Q{i+1}: {q}")
    #print(f"A{i+1}: {a}\n")


################
#Hier I should take the row number from mod1_randomquestion
#and get the answer