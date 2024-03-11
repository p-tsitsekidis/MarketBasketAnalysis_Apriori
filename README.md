# Information Retrieval and Data Mining Project

## Overview
This project explores the application of data mining techniques to real-world sales data to uncover patterns and insights. Using data mining tools such as WEKA, alongside Python for data preprocessing, we delve into the Apriori algorithm for frequent pattern mining. The goal is to demonstrate the practical use of data mining algorithms in analyzing and deriving meaningful conclusions from sales data.

## Tools Used
- Python: Data preprocessing to make the dataset compatible with WEKA.
- WEKA: Application of the Apriori algorithm for pattern mining.

## Objectives
- To apply data mining techniques to real sales data.
- To extract frequent patterns using the Apriori algorithm.
- To interpret the results and gain insights into the sales data.

## Data
The analysis is based on two datasets:
- `customerBuys.csv`: Contains records of customer purchases. Purchases in the same date means in the same transaction.
- `customerAge.csv`: Contains customer age data along with the customer's ID.

## Python Enviroment
- To set the enviroment for python, run in the terminal the following command:
"pip install -r requirements.txt"

## Project Structure
This project is organized into several folders, each dedicated to specific tasks and analyses. Below is an overview of what each folder contains:

### Task 1: Data Preprocessing and Popularity Analysis

#### Folder: `Task1/`

#### Description:
In Task 1, we focus on preprocessing sales data and conducting a popularity analysis of products sold. The script performs several key operations:

- **Popularity Analysis:**
  - **Product Popularity:** We calculate the frequency of purchases for each product to determine their popularity. This information is saved to `product_popularity_data.csv` and visualized in two plots: the top 20 most popular products and the bottom 20 least popular products, showcasing the sales distribution across different products in our inventory.
  - **Sales Trends Over Time:** The script converts the `Date` column to datetime format for temporal analysis. It then filters sales data for the years 2022 and 2023, aggregating monthly sales to observe trends over these periods. This analysis helps in understanding seasonal sales patterns, visualized in a line plot comparing monthly sales between the two years.
  - **Top Product Per Month:** Additionally, we analyze which product was the most sold for each month, providing insights into changing consumer preferences over time. This data is compiled into `top_product_per_month.csv`.

- **Customer Analysis:** Finally, the script identifies the top 10 customers based on the frequency of their purchases, not the total amount spent. This highlights our best customers by engagement, visualized in a bar plot.

#### Contents:
- `customerBuys.csv`: The dataset containing records of customer purchases.
- `product_popularity_data.csv`: A CSV file listing products by their purchase frequency.
- `top_product_popularity_plot.png`: A bar plot showing the top 20 most popular products.
- `bottom_product_popularity_plot.png`: A bar plot showing the bottom 20 least popular products.
- `monthly_sales_2022_2023.png`: A line plot visualizing monthly sales for 2022 and 2023.
- `top_product_per_month.csv`: A CSV file detailing the most popular product for each month.
- `top_customers_by_frequency.png`: A bar plot highlighting the top 10 customers by the number of purchases.


### Task 2: Data Transformation for WEKA Analysis

#### Folder: `Task2/`

#### Description:
Task 2 focuses on transforming the sales data into a format compatible with WEKA for frequent pattern mining. Key steps include:

- **Unique Transaction Identification:** Assigning a unique `GroupID` to each transaction based on `CustomerID` and `Date`.
- **Binary Matrix Creation:** Constructing a binary matrix to represent the presence (`'y'`) or absence (`'?'`) of each product in transactions, crucial for WEKA's analysis.
- **Data Transformation:** Saving the binary matrix to `binary_matrix.csv`. After the conversion to .arff the file is ready for input into WEKA to discover frequent buying patterns.

#### Contents:
- `binary_matrix.csv`: The dataset transformed into a binary format, indicating product presence or absence in transactions.
- `binary_matrix.arff`: The .arff file is what we need to use in WEKA.

### Task 5: Grouping Products and Binary Matrix Transformation

#### Folder: `Task5/`

#### Description:
Task 5 extends the data preparation for WEKA analysis by grouping products into categories and generating a new binary matrix. This task is divided into two main scripts:

- **`convert.py`:** Transforms sales data into a binary matrix indicating the presence or absence of products in transactions, similar to Task 2 but with grouped product categories.
- **`group.py`:** Maps individual products to their respective categories based on predefined groupings. This categorization simplifies the analysis by focusing on product types rather than individual items, facilitating broader pattern discovery.

#### Process:
1. **Grouping Products:** Using `group.py`, products are categorized into groups such as 'Dairy Products', 'Meat Products', etc., based on a predefined mapping. This helps in analyzing patterns at a category level.
2. **Binary Matrix Creation:** `convert.py` takes the grouped transactions and creates a binary matrix, which is then used for pattern mining in WEKA.

#### Contents:
- `customerBuys_Groups.csv`: Contains transactions with products mapped to their respective categories.
- `binary_matrix.csv`: The binary matrix given by the script.
- `binary_matrix.arff`: The file we use in WEKA.

### Task 6: Integrating Age Data and Segment Analysis

#### Folder: `Task6/`

#### Description:
Task 6 enriches the dataset by merging customer age information with purchase data, allowing for an analysis segmented by age groups. It involves three scripts to prepare the data for pattern mining considering customer age segments:

- **`merge.py`:** Merges purchase data with customer age, assigns unique transaction IDs, and creates a binary matrix for products, incorporating an 'Age' column.
- **`age_groups.py`:** Defines age bins (18-35, 36-60, 60-80), categorizes customers into these age groups, and aggregates purchase data by age group. The output is saved in CSV files for each age group.
- **`transactions_by_age_group.py`:** Prepares binary matrices for each age group, tailored for analysis in WEKA by dropping unnecessary columns and ensuring data compatibility.

#### Contents:
- `binary_matrix_18-35.arff`: ARFF file for transactions by customers aged 18-35, ready for WEKA analysis.
- `binary_matrix_18-35.csv`: CSV file for transactions by customers aged 18-35, detailing product presence.
- `binary_matrix_36-60.arff`: ARFF file for transactions by customers aged 36-60, ready for WEKA analysis.
- `binary_matrix_36-60.csv`: CSV file for transactions by customers aged 36-60, detailing product presence.
- `binary_matrix_60-80.arff`: ARFF file for transactions by customers aged 60-80, ready for WEKA analysis.
- `binary_matrix_60-80.csv`: CSV file for transactions by customers aged 60-80, detailing product presence.
- `binary_matrix_with_age.csv`: Comprehensive CSV including all transactions with an additional column for customer age.
- `groupby.csv`: Data aggregated by specific criteria, not further specified.
- `merged.csv`: Dataset from merging purchase data with additional attributes like customer age.
- `purchases_18-35.csv`: Summarized purchases for customers aged 18-35, aggregating product buying patterns.
- `purchases_36-60.csv`: Summarized purchases for customers aged 36-60, aggregating product buying patterns.
- `purchases_60-80.csv`: Summarized purchases for customers aged 60-80, aggregating product buying patterns.
