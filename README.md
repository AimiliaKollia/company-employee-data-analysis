# company-employee-data-analysis
Python program to process and analyze company employee data from CSV and JSON files in order to extract meaningful insights
Final Project Program: Processing Employee Data for the HR Department of a Company
Full name: Aimilia Kollia

Project Overview::
This project is designed to process and analyze employee data for a fictional company using Python. The data includes information 
about employees such as their id, first name, last name, email, gender, department, salary, bonus, and date of birth. The purpose 
of the project is to practice handling data files (CSV/JSON format), validating user inputs, and performing various operations 
on this data in order to extract meaningful insights. 

Scenario:
In this scenario, I am working with a company that has a diverse set of employees working in various departments. 
The data was generated using Mockaroo, a tool for creating mock data, and contains 100 rows of sample employee data.
The company has the following departments: Research and Development, Support, Engineering, Business Development, 
Accounting, Legal, Marketing, Sales, Training, Product Management, and Human Resources. 
Each employee's salary and bonus may vary, and some of the bonus fields are left blank for a percentage of the employees.

Data Format:
The employee data is in a CSV format with the following columns:
1.	id: A unique identifier for each employee.
2.	first_name: The first name of the employee.
3.	last_name: The last name of the employee.
4.	email: The email address of the employee.
5.	gender: The gender of the employee (e.g., Male, Female, Non-binary).
6.	department: The department each employee works in (e.g., Research and Development, Human Resources, Marketing).
7.	salary: The salary of the employee.
8.	bonus: The bonus of the employee (some values may be missing).
9.	dateOfBirth: The birthdate of the employee (in DD/MM/YYYY format).

Folder Structure
	Kollia-project/
	 README.txt: This file, describing the project scenario and data.
	 task1.py: Solution to Task 1.
	 task2.py: Solution to Task 2.
	 employee.py: Defines employee object (part of task 3)
     task3_test: Creates two test objects and tests functionality defined in employee object (part of task 3)
     task3.py: Solution to task 3.
	 task4.py: Solution to Task 4.
	 company_data.csv: CSV file containing the generated dataset.
	 company_data.json: JSON file containing the generated dataset.
     validation_module.py: input validation function code meant to be reused and inputed in more than one programs

The project contains 4 separate tasks.

Task Description: 

Task 1 – Files, Input/Output, String/Number Manipulation, Lists:
This creates a python program that: 
1.	Reads the CSV file (without using CSV import).
2.	Asks the user for a filename and handles invalid inputs.
3.	Reads the file line by line and splits the content using the string split method.
4.	Skips the header if present.
5.	Sorts the data by department and full name.
6.	Prompts the user to input how many rows to display, with validation (using validation_module.py). 
    And repeats the question until the user's input is valid.
7.	Displays the formatted data.

Task 2 – Reading CSV Files, Lists, Sets, Dictionaries and Manipulating Data:
This creates a program that:
1.  Loads the previous csv file, but now using csv reader and reads the information in a list of dictionaries.
2.  Creates a set of unique values for a grouped field (a set of all department names).
3.  Counts how many employees exist in each department.
4.  Calculates the total number of employees, the sum of salaries and the average salary.
5.  Asks the user to enter a number of rows from 0 to 100 to display and validates that the user does that (using validation_module.py). 
6.  Displays the output in a formatted way.

Task 3 – OOP, JSON:
This task consists of 3 parts which are contained in the files called "employee.py", "task3_test.py" and "task3.py".

a. employee.py:
1. Imports the json file that was generated.
2. Defines an employee object, with all the instance attributes included in the JSON file.
3. The employee object contains one class attribute which will have an initial value (in this case the name of the company),
   and also contains the __init__ method and the __str__(self) method (to produce a formatted result of all information in the object).

b. task3_test.py:
1. Imports the employee object.
2. In the main method it creates 2 test objects by providing my own values.
3. Calls the methods to showcase the functionality defined in the employee object.

c. task3.py:
1. Imports the employee object.
2. Loads the company_data json file into a list of objects.
3. Displays a menu for the user.
4. Accepts an option from the menu and validates the user's input.
5. Performs the task that the user has selected and displays the output in a formatted way.

Task 4 -  Web Services, Pandas, MatPlotLib
This code retrieves data from a web API, processes it using Pandas and performs the following tasks
Uses the URL generated from Mockaroo
1. Handles missing values by replacing them with default values (0 for numeric, 'NA' for character fields).
2. Creates a new column ('TotalSalary') by adding 'salary' and 'bonus'.
3. Displays descriptive statistics of the dataset.
4. Groups the data by 'department' to count the number of rows per department.
5. Creates a subset of employees with a salary greater than 5000 for further analysis.
6. Generates two meaningful plots: a histogram of salary distribution and a bar chart of average salary by department.
The goal is to analyze and visualize the dataset to identify trends and patterns.

