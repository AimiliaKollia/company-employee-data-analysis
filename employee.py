# employee.py
# Full Name: Aimilia Kollia
# # This code defines an Employee class to represent an employee's information and provide functionalities 
# such as giving a percentage salary raise and calculating total compensation. The class is initialized with 
# attributes from the JSON file that we are using and includes methods for formatted output and specific operations related to 
# employee salary and bonus.
import json

class Employee:
    company_name = "TechCorp"  # Class attribute with the company name

    def __init__(self, id: int, first_name: str, last_name: str, email: str, gender: str, department: str, salary: float, bonus: float, dateOfBirth: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.department = department
        self.salary = salary
        self.bonus = bonus if bonus else 0.0    # Default to 0.0 if the bonus is None
        self.dateOfBirth = dateOfBirth

    def __str__(self):
        # Gives a formatted string with the employee information.
        output =  f"ID: {self.id}, Full Name: {self.first_name} {self.last_name}, " \
        f"Email: {self.email}, Gender: {self.gender}, Department: {self.department}, " \
        f"Salary: {self.salary:.2f}, Bonus: {self.bonus:.2f}, DateOfBirth: {self.dateOfBirth}"

        return output

    # Instance method 1 giving a percentage salary raise. Updates the salary attribute by increasing it by the specified percentage.
    def give_pct_salary_raise(self, percent):
        increase = self.salary * (percent / 100)
        self.salary += increase
        return f"Salary updated. New Salary: ${self.salary:.2f}"

    # Instance method 2 calculating total compensation (salary + bonus). Calculates and returns the sum of salary and bonus.
    def calculate_total_compensation(self):
        total = self.salary + self.bonus
        return f"Total Compensation: ${total:.2f}"
