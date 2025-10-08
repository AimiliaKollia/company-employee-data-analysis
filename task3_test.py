# task3_test.py
#Full Name: Aimilia Kollia
# This code tests the Employee class by creating two test objects and demonstrating 
# its functionality, including the __str__ method, salary raise method, and total compensation calculation.

from employee import Employee

def main():
    # Creating the first test object
    employee1 = Employee(
        id=1,
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        gender="Male",
        department="Engineering",
        salary=6000,
        bonus=1500,
        dateOfBirth="1990-01-01"
    )

    # Creating the second test object
    employee2 = Employee(
        id=2,
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        gender="Female",
        department="Marketing",
        salary=5000,
        bonus=1000,
        dateOfBirth="1985-02-15"
    )

    # Displaying information for both employees using the __str__ method
    print("Employee 1 Details:")
    print(employee1)
    print("\nEmployee 2 Details:")
    print(employee2)

    # Calling the give_pct_salary_raise method for both employees
    print("\nGiving a 10% raise to Employee 1...")
    print(employee1.give_pct_salary_raise(10))

    print("\nGiving a 20% raise to Employee 2...")
    print(employee2.give_pct_salary_raise(20))

    # Calling the calculate_total_compensation method for both employees
    print("\nCalculating total compensation for Employee 1:")
    print(employee1.calculate_total_compensation())

    print("\nCalculating total compensation for Employee 2:")
    print(employee2.calculate_total_compensation())

if __name__ == "__main__":
    main()

