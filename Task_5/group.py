import pandas as pd

# Load Data
unique_items_path = '/home/petros/Desktop/mini_market/Task_1/product_popularity_data.csv'
purchases_path = '/home/petros/Desktop/mini_market/customerBuys.csv'

unique_items_df = pd.read_csv(unique_items_path)

# Create a dictionary mapping from product names to group names based on line numbers
product_groups = {
    'Dairy Products': [2, 6, 23, 26, 27, 31, 38, 44, 54, 56, 64, 65, 79, 80, 94, 151],
    'Meat Products': [10, 19, 21, 25, 30, 37, 45, 46, 75, 78, 88, 106, 119, 128, 135, 160],
    'Vegetables': [3, 7, 29, 39, 62, 69, 71, 87, 93, 95, 131, 133, 153],
    'Fruits': [8, 11, 13, 36, 53, 138, 152],
    'Alcoholic Beverages': [15, 16, 48, 50, 57, 61, 63, 97, 110, 117, 123, 142, 156, 158],
    'Non-Alcoholic Beverages': [5, 9, 24, 28, 101, 131, 147],
    'Pastries': [4, 12, 20, 32, 41, 42, 66, 67, 73, 102],
    'Snacks/Sweets': [17, 33, 34, 40, 49, 51, 55, 59, 81, 83, 96, 103, 109, 113, 120, 121, 132, 134, 136, 149, 150],
    'Cooking Ingredients': [43, 52, 72, 82, 84, 90, 105, 112, 115, 124, 129, 139, 145, 159],
    'Household and Cleaning Products': [14, 35, 58, 68, 70, 74, 77, 91, 92, 111, 114, 125, 126, 130, 137, 143, 144, 155, 161, 163, 166],
    'Personal Care Products': [116, 118, 122, 140, 141, 157, 162, 165],
    'Pet-Care Products': [60, 85, 98],
    'Miscellaneous': [18, 89, 99, 100, 146, 164, 167],
    'Foods': [22, 47, 76, 86, 104, 107, 108, 127, 148, 154]
}

# Inverting the dictionary for easier lookup
line_to_group = {}
for group, lines in product_groups.items():
    for line in lines:
        # Adjust for 0-based indexing
        product_name = unique_items_df.loc[line - 2, 'Product']  # -2 because of 0-index and header row
        line_to_group[product_name] = group

# Load the purchase transactions
purchases_df = pd.read_csv(purchases_path)

# Map products to their groups
purchases_df['Product'] = purchases_df['Product'].map(line_to_group)

purchases_df.to_csv('customerBuys_Groups.csv', index=False)
