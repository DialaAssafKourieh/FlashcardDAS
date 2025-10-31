#define a module that compare the
#  answer with the correct answer
import pandas as pd
df = pd.read_excel('Flashcardsdata1.xlsx', sheet_name='BIOLOGY')
question = df['Questions']
Answer=df['Answers']
#print('The Question is :',question)
print("The Answer:", Answer)
