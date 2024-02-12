import pandas as pd

df = pd.read_csv('/home/petros/Desktop/mini_market/customerBuys.csv')

# Create a unique identifier for each transaction
df['TransactionID'] = df.groupby(['CustomerID', 'Date']).ngroup()

# Create a binary matrix
binary_matrix = pd.crosstab(index=df['TransactionID'], columns=df['Product'])

# Convert all non-zero values to 1
for column in binary_matrix.columns:
    binary_matrix[column] = binary_matrix[column].apply(lambda x: 'y' if x != 0 else '?')

# Optionally, reset the index to make 'TransactionID' a column
binary_matrix.reset_index(inplace=True)

binary_matrix = binary_matrix.drop(columns=['TransactionID'])

# Save the binary matrix to a CSV file
binary_matrix.to_csv('binary_matrix.csv', index=False)