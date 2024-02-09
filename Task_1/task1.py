import pandas as pd
import matplotlib.pyplot as plt

buys = ['CustomerID', 'Date', 'Product']
age = ['CustomerID', 'Age']

# Load the Data
customer_buys = pd.read_csv('/home/petros/Desktop/mini_market/customerBuys.txt', delimiter='\t', names=buys)
customer_age = pd.read_csv('/home/petros/Desktop/mini_market/customerAge.txt', delimiter='\t', names=age)

# Merging customer_buys with customer_age
merged_data = pd.merge(customer_buys, customer_age, on='CustomerID')
merged_data.to_csv('/home/petros/Desktop/mini_market/Task_1/merged_customer_data.csv', index=False)

# Popularity
product_counts = customer_buys['Product'].value_counts().sort_values(ascending=False)
product_counts.to_csv('product_popularity_data.csv', header=['Number of Purchases'])
top_product_counts = customer_buys['Product'].value_counts().sort_values(ascending=False).head(20) # Show top 20.
plt.figure(figsize=(20, 10))
top_product_counts.plot(kind='bar')
plt.title('Most Popular')
plt.xlabel('Product')
plt.ylabel('Number of Purchases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_product_popularity_plot.png')
plt.show()

bottom_product_counts = customer_buys['Product'].value_counts().sort_values(ascending=True).head(20) # Show bottom 20.
plt.figure(figsize=(20, 10))
bottom_product_counts.plot(kind='bar')
plt.title('Least Popular')
plt.xlabel('Product')
plt.ylabel('Number of Purchases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bottom_product_popularity_plot.png')
plt.show()

# Sales by Month
customer_buys['Date'] = pd.to_datetime(customer_buys['Date'])

# Filter years
filter_2022 = customer_buys['Date'].dt.year == 2022
sales_2022 = customer_buys[filter_2022] # Boolean Series Indexing.
filter_2023 = customer_buys['Date'].dt.year == 2023
sales_2023 = customer_buys[filter_2023]

monthly_sales_2022 = sales_2022.groupby(sales_2022['Date'].dt.month).size()
monthly_sales_2023 = sales_2023.groupby(sales_2023['Date'].dt.month).size()

# Month popularity for each year
plt.figure(figsize=(12, 6))
monthly_sales_2022.plot(kind='line', marker='o', label='2022')
monthly_sales_2023.plot(kind='line', marker='o', label='2023')
plt.title('Total Sales per Month for 2022 and 2023')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.legend()
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.tight_layout()
plt.savefig('monthly_sales_2022_2023.png')
plt.show()

# Best customers based on buying frequency, not by total amount spent.
best_customers = customer_buys.groupby(customer_buys['CustomerID']).size().sort_values(ascending=False)
top_customers = best_customers.head(10)

plt.figure(figsize=(12, 6))
top_customers.plot(kind='bar')
plt.title('Top 10 Customers by Number of Purchases')
plt.xlabel('Customers')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('top_customers_by_frequency.png')
plt.show()