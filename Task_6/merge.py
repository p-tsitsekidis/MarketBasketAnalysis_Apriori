import pandas as pd

buys = pd.read_csv('/home/petros/Desktop/mini_market/Task_5/customerBuys_Groups.csv')
age = pd.read_csv('/home/petros/Desktop/mini_market/customerAge.csv')

# Merge to include age
merged_df = pd.merge(buys, age, on='CustomerID')

# Assign a unique group ID for each transaction
merged_df['GroupID'] = merged_df.groupby(['CustomerID', 'Date']).ngroup()

# Create the binary matrix for products
binary_matrix = pd.crosstab(index=merged_df['GroupID'], columns=merged_df['Product'])

age_mapping = merged_df[['GroupID', 'Age']].drop_duplicates().set_index('GroupID')['Age']

# Map Age
binary_matrix['Age'] = binary_matrix.index.map(age_mapping)

binary_matrix.to_csv('binary_matrix_with_age.csv', index=False)