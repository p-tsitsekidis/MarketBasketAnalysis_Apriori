import pandas as pd

df = pd.read_csv('/home/petros/Desktop/mini_market/Task_5/customerBuys_Groups.csv')

df['GroupID'] = df.groupby(['CustomerID', 'Date']).ngroup()

binary_matrix = pd.crosstab(index=df['GroupID'], columns=df['Product'])
binary_matrix = binary_matrix.map(lambda x: 'y' if x > 0 else '?')

binary_matrix.reset_index(drop=True, inplace=True)

binary_matrix.to_csv('binary_matrix.csv', index=False)