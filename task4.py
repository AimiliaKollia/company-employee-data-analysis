# task4.py
# Full name: Aimilia Kollia
# # This code retrieves data from a web API, processes it using Pandas, 
# and performs the following tasks:
# 1. Handles missing values by replacing them with default values (0 for numeric, 'NA' for character fields).
# 2. Creates a new column ('TotalSalary') by adding 'salary' and 'bonus'.
# 3. Displays descriptive statistics of the dataset.
# 4. Groups the data by 'department' to count the number of rows per department.
# 5. Creates a subset of employees with a salary greater than 5000 for further analysis.
# 6. Generates two meaningful plots: a histogram of salary distribution and a bar chart of average salary by department.
# The goal is to analyze and visualize the dataset to identify trends and patterns.
import pandas as pd
import requests

# Step 1: Calling the web service
url = "https://my.api.mockaroo.com/company_data.json?key=c7f3b500"
response = requests.get(url)
results = response.json()

# Step 2: Converting JSON response to a Pandas DataFrame
df = pd.json_normalize(results)

# Step 3: Handling missing values
# Replacing missing numeric values with 0
numeric_cols = df.select_dtypes(include=["number"]).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Replace missing character values with 'NA'
char_cols = df.select_dtypes(include=["object"]).columns
df[char_cols] = df[char_cols].fillna("NA")

# Step 4: Creating a new column with a calculation
df['TotalSalary'] = df['salary'] + df['bonus']

# Step 5: Displaying descriptive statistics
print("Descriptive Statistics:")  # It displays descriptive statistics only for numeric columns (e.g salary etc.)
print(df.describe())

# Step 6: Grouping by a specific field (e.g., Department) and counting rows
grouped = df.groupby('department').size()
print("\nRows per department:")
print(grouped)

# Step 7: Creating a meaningful subset of the data
# Subset: Employees with salaries greater than 5000
high_salary_subset = df[df['salary'] > 5000]
print("\nSubset of employees with salary > 5000:")
print(high_salary_subset)

# Purpose of the subset: Identify high earners for bonus distribution or promotions.

# Step 8: Create plots
import matplotlib.pyplot as plt

# Plot 1: Distribution of salaries
# It displays the distribution of salaries using a histogram,
# which is good for visualizing how salaries are distributed across employees.
plt.figure(figsize=(10, 6))
plt.hist(df['salary'], bins=10, color='blue', edgecolor='black') # Histogram bins are the ranges into which the data is grouped in the histogram.
plt.title('Distribution of Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
# We have a range of values from 0 to 100, and we set the bin width of the histogram to 10, 
# therefore the bins will represent the ranges [0-10], [10-20], [20-30], and so on.

# Plot 2: Average salary by department
# This bar plot shows the average salary by department, 
# which is a useful visualization to understand salary trends across departments.
avg_salary_by_dept = df.groupby('department')['salary'].mean()
avg_salary_by_dept.plot(kind='bar', figsize=(10, 6), color='orange', edgecolor='black')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.show()
