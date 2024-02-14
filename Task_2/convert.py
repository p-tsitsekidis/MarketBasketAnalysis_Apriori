import pandas as pd

df = pd.read_csv('/home/petros/Desktop/mini_market/customerBuys.csv')

# Find each unique transaction
df['GroupID'] = df.groupby(['CustomerID', 'Date']).ngroup()

# Create a binary matrix
binary_matrix = pd.crosstab(index=df['GroupID'], columns=df['Product'])

# 'y' for bought item and '?' for the absence of an item (for WEKA)
binary_matrix = binary_matrix.map(lambda x: 'y' if x > 0 else '?')

# Remove the index, we only want the item names as columns
binary_matrix.reset_index(drop=True, inplace=True)

# Result
binary_matrix.to_csv('binary_matrix.csv', index=False)