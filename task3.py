# task3.py
#Full name: Aimilia Kollia
# This code provides a menu-driven program to interact with employee data loaded from a JSON file. 
# It allows displaying all employee information, searching by various attributes, filtering employees 
# based on numeric attributes, and exiting the program. The script utilizes the Employee class to represent 
# individual employees and their properties, with formatted outputs for better usability.

import json
from employee import Employee


def load_employees_from_json(filename):
    # Loading the employees from our JSON file and returns a list of employee objects.
    employees = [] # Creating an empty list to store employee objects
    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data: # Iterating over each employee item in the company_data JSON file
            # Creating an Employees object using data from the company_data JSON file and adding it to the employees list
            employees.append(
                Employee(
                    id=item['id'],
                    first_name=item['first_name'],
                    last_name=item['last_name'],
                    email=item['email'],
                    gender=item['gender'],
                    department=item['department'],
                    salary=item['salary'],
                    bonus=item['bonus'],
                    dateOfBirth=item['dateOfBirth']
                )
            )
    return employees # It returns the list of employee objects.


def display_menu():
    # Displays the menu options for the program to the user.
    print("1. Display all the information")
    print("2. Search by <<any attribute>>")
    print("3. Display all rows with a <<numeric attribute>> more than a user-entered value")
    print("4. Exit")


def display_all(employees):
    # Displaying all of the employee details.
    print("\n--- All Employees ---")
    for emp in employees:
        print(emp)
    print("\n")


def search_by_attribute(employees, attribute, value):
    # It searches for employees by a specific attribute and value.
    print(f"\n--- Searching by {attribute} = {value} ---")
    # Tracks whether any employee matches the search criteria
    found = False # Initially, there is no match, so it is set to False.

    # Iterating over each employee from the list of the employees
    for emp in employees:
        # Checking each attribute
        if attribute == "id" and emp.id == int(value):# Checking weather the search attribute is 'id' and if the employee's id matches the given value
            print(emp) # Prints the employee details if it finds a match
            found = True # Sets to 'True' as it finds a match
        elif attribute == "first_name" and emp.first_name.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "last_name" and emp.last_name.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "email" and emp.email.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "gender" and emp.gender.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "department" and emp.department.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "salary" and emp.salary == float(value):
            print(emp)
            found = True
        elif attribute == "bonus" and emp.bonus == float(value):
            print(emp)
            found = True
        elif attribute == "dateOfBirth" and emp.dateOfBirth == value:
            print(emp)
            found = True
    # If it doesn't find any matching employees it prints the following message
    if not found:
        print("No matching employees found.\n")

def filter_by_numeric_attribute(employees, attribute, given_user_value):
    # Displays all of the employees whose numeric attribute is greater than value that the user gave,
    # by using int() or float() conversion directly.
    print(f"\n---- Employees with {attribute} higher than {given_user_value} ----")
    found = False # Tracks if any matching employees are found

    for emp in employees: # Iterating over each employee in the list of employees
        try:
            # Checks if the attribute is 'id' and if the employee's id is greater than the given value
            if attribute == "id" and emp.id > int(given_user_value):
                print(emp) # Prints the employee details if they match the condition
                found = True # Sets to True as it finds a match 
            elif attribute == "salary" and emp.salary > float(given_user_value):
                print(emp)
                found = True
            elif attribute == "bonus" and emp.bonus > float(given_user_value):
                print(emp)
                found = True
        except:
            print("Invalid input.Please enter a valid numeric value for comparison.")
            return
    if not found: # It displays the following message after the loop if there are no employees that match
        print("No employees found.")




def main():
    # Loads the employees from the company_data JSON file.
    filename = "company_data.json"  # Replaces with the actual name of my JSON file
    employees = load_employees_from_json(filename)

    while True:
        display_menu() # calling the function
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_all(employees) # calling the function
        elif choice == '2':
            attribute = input("Enter the attribute to search by (id, first_name, last_name, department, email, gender, salary, bonus, dateOfBirth): ").strip()
            value = input(f"Enter the value for {attribute}: ").strip()
            search_by_attribute(employees, attribute, value) # calling the function
        elif choice == '3':
            attribute = input("Enter the attribute you want to search for a numeric value(id, salary, bonus): ").strip()
            try:
                given_user_value = float(input(f"Enter the minimum value for {attribute}: "))
                filter_by_numeric_attribute(employees, attribute, given_user_value) # calling the function
            except:
                print("Invalid entered value. Please enter a numeric value.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
