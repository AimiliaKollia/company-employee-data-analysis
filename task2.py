# task2.py 
# Full name: Aimilia Kollia
# This program loads the previous CSV file containing company data into a list of dictionaries and reads it.
# It creates a set of unique values for the grouped field for department.
# It processes the data to count how many employees exist in each group (e.g. department),
# and produces some statistics like the sum of salaries and the average salary of the employees.

import csv

from validation_module import get_valid_input  # Importing the validation function from the file validation_module.py

def load_data(filename):
    #Loading the CSV data into a list of dictionaries.
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file) # The csv.DictReader reads the csv file and maps each row to a dictionary. The keys for the dictionary are derived from the first row(header) of the csv file
            for row in reader:
                data.append(row)  # Adding each row from the csv to the data list as a dictionary
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

def get_unique_groups(data, field):
    # Creating a set of unique values for the given grouped field.
    unique_values = set()
    for row in data:
        unique_values.add(row[field])  # Adding each unique field value to the set
    return unique_values

def count_group_field(data, field):
    # Counts how many employees exist in each group data field.
    count_dict = {}
    unique_values = get_unique_groups(data, field)  # Get unique department names
    for value in unique_values:
        count_dict[value] = sum(1 for row in data if row[field] == value)
    return count_dict

def calculate_statistics(data):
    # Calculating statistics: sum of salaries and average salary.
    # We use the 'salary' field for calculating the total salary,and then again the 'salary' field 
    # to calculate the average salary of employees.
    # The sum of salaries and the average salary of the employees was selected as a statistical calculation
    # because its important for the company to be able to compare these two parameters
    # in order to see how much is the total amount they are spending on salaries compared to their budget
    # and if there needs to be an increase or decrease of the average salary of their employees.
    total_salary = 0
    for row in data:
        total_salary += int(row['salary'])  # Sums up salary values

    # Calculates the average salary by dividing the total salary by the number of employees
    average_salary = total_salary / len(data) if len(data) > 0 else 0
    return total_salary, average_salary

def main():
    # Main function of the program.

    # Asking for the filename (the default filename is 'company_data.csv')
    filename = input("Enter the filename (or press Enter for default 'company_data.csv'): ")

    if not filename:  # If no filename is entered, use the default file name
        filename = 'company_data.csv'

    # Loading data from the CSV file
    data = load_data(filename)
    if data is None:
        return  # Exits the program if file loading fails

    # Counting how many employees exist for each department
    department_count = count_group_field(data, 'department')

    # Calculating statistics: total salary and average salary
    total_salary, average_salary = calculate_statistics(data)

    # Ask the user for the number of rows to display and validate input
    num_rows = get_valid_input()

    # Display the department-wise employee count (show only limited rows)
    print("\nDepartment # of Employees")
    print("------------------ ---------------------")

    # We limit the number of rows to display as per the user's input (in this case, department count)
    departments_to_display = list(department_count.items())[:num_rows]
    for key, value in departments_to_display:
        print(f"{key:<20} {value:<10}")

    # Display statistics
    print("\nStatistics")
    print("----------------------------------------------")
    print(f"Total number of employees: {len(data)}")
    print(f"Sum of Salaries: {total_salary}")
    print(f"Average Salary: {average_salary:.2f}")

# Run the program when executed
if __name__ == "__main__":
    main()

