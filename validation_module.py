# validation_module.py
# Full name: Aimilia Kollia
# The get_valid_input function prompts the user to enter a valid number of rows to display (between 0 and 100). 
# It is meant to be used in my other programms to reduce lines of code and save some time.
def get_valid_input():
    # Prompting the user to enter a valid number of rows to display.
    while True:
        try:
            num_rows = int(input("How many rows do you want to display? "))
            if 0 <= num_rows <= 100:
                return num_rows
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
