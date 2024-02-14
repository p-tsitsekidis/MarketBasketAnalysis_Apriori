import pandas as pd

# Load the dataset
df = pd.read_csv('/home/petros/Desktop/mini_market/Task_5/customerBuys_Groups.csv')

# Find each unique transaction
df['GroupID'] = df.groupby(['CustomerID', 'Date']).ngroup()

# Create a binary matrix
binary_matrix = pd.crosstab(index=df['GroupID'], columns=df['Product'])

# 'y' for bought item and '?' for the absence of an item
binary_matrix = binary_matrix.map(lambda x: 'y' if x > 0 else '?')

# Remove the index
binary_matrix.reset_index(drop=True, inplace=True)

# Result
binary_matrix.to_csv('binary_matrix.csv', index=False)