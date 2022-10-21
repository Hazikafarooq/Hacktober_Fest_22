import pandas as pd
df = pd.read_csv('file_name.csv')
print(df)

pd.read_csv('file_name.csv', usecols=['column_name1', 'column_name2'])
pd.read_csv('file_name.csv', sep='\t')
