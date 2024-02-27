import pandas as pd

binary_matrix = pd.read_csv('binary_matrix_with_age.csv')

# Define age bins and labels for the groups
age_bins = [18, 35, 60, 80]
age_labels = ['18-35', '36-60', '60-80']

# Categorize each customer's age into age groups
binary_matrix['AgeGroup'] = pd.cut(binary_matrix['Age'], bins=age_bins, labels=age_labels, right=False)

# Group by the age group and sum purchases within each group
grouped_purchases = binary_matrix.groupby('AgeGroup').sum()

# Drop the 'Age' column since it's no longer needed in the summed data
grouped_purchases = grouped_purchases.drop(columns='Age')

# Iterate over each age group to save their data to separate CSV files
for age_group in age_labels:

    # Filter the data for the current age group
    age_group_data = grouped_purchases.loc[age_group]

    # Sort the data
    age_group_data = age_group_data.sort_values(ascending=False)
    
    # Save to CSV
    age_group_data.to_csv(f'purchases_{age_group}.csv')