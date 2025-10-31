#this program read Excelfile column and 
# sum the amount of each column

print('Hello Diala')
import pandas as pd
df = pd.read_excel('Excelfile.xlsx', sheet_name='sheet1')
lm=pd.read_excel('Excelfile.xlsx',sheet_name='sheet1')
total1 = df['number1'].sum()
total2=df['number2'].sum()
print('The numbers are :',lm)
print("Total number1:", total1)
print("total number2",total2)