import pandas as pd

# Load the dataset with transactions and ages
binary_matrix_with_age = pd.read_csv('binary_matrix_with_age.csv')

# Define age bins and labels for the groups
age_bins = [18, 35, 60, 80]
age_labels = ['18-35', '36-60', '60-80']

# Categorize each customer's age into age groups
binary_matrix_with_age['AgeGroup'] = pd.cut(binary_matrix_with_age['Age'], bins=age_bins, labels=age_labels, right=False)

# Prepare a list to collect group dataframes
group_dataframes = []

# Iterate over each age group
for age_group in age_labels:
    # Filter transactions for the current age group
    transactions_age_group = binary_matrix_with_age[binary_matrix_with_age['AgeGroup'] == age_group]

    # Drop the 'Age' and 'AgeGroup' columns as they are not needed for the Apriori algorithm
    transactions = transactions_age_group.drop(columns=['Age', 'AgeGroup'])

    transactions = transactions.map(lambda x: 'y' if x > 0 else '?')

    # Save the binary matrix for the current age group to a CSV file
    transactions.to_csv(f'binary_matrix_{age_group}.csv', index=False)

    # Collect the dataframe for potential future use
    group_dataframes.append(transactions)