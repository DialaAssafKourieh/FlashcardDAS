import pandas as pd
df = pd.read_excel('Flashcardsdata1.xlsx', sheet_name='BIOLOGY')
first_field = df.iloc[0, 0]  # first row, first column
print("First field in Excel:", first_field)
