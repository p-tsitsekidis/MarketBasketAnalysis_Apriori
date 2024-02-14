import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('binary_matrix_with_age.csv')

# Aggregation
total_purchases_by_age = df.groupby('Age').sum().reset_index()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Age', y='Dairy Products', data=total_purchases_by_age, palette='viridis')
plt.title('Total Purchases of Dairy Products by Age')
plt.xlabel('Age')
plt.ylabel('Total Purchases')
plt.xticks(rotation=45)
plt.savefig('Dairy_products_by_age.png')
plt.show()
