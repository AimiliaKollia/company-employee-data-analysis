# task1.py 
# Full name: Aimilia Kollia
# This program loads a CSV file containing company data, processes the data,
# and displays a sorted and formatted output. The user can input a filename
# and select the number of rows of information to display.

from validation_module import get_valid_input  # Importing the validation function from the file validation_module.py

def load_data(filename):
    # Loading CSV data from the file and returning it as a list of lists.
    data = []
    try:
        with open(filename, 'r') as file:
            # Skipping the header by calling next() once
            next(file)
            # Reading each line, splitting it by commas, and appending to the data list
            for line in file:
                data.append(line.strip().split(','))
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None

def sort_data(data):
    # Sorting the data by department (the "group field") and then by employee last_name (the "detailed field").
    # Sorting first by department(index 5) and secondly by the employees last name(index 2) makes sense 
    # for the user because this sorting ensures that rows of employees of the same department are grouped together 
    # to be better organised and able to locate. Within those groups, the rows are sorted by employee last name.
    return sorted(data, key=lambda x: (x[5], x[2]))  # Sort by department (x[5]) and then by employee last name (x[2])

def main():
    """Main function of the program."""

    # Asking for the filename (The default filename is 'company_data.csv')
    filename = input("Enter the filename (or press Enter for default 'company_data.csv'): ")

    if not filename:  # If no filename is entered, it uses the default file name
        filename = 'company_data.csv'

    # Loading the data from the CSV file
    data = load_data(filename)
    if data is None:
        return  # Exiting the program if the file fails to load

    # Sorting the data
    sorted_data = sort_data(data)

    # Asking the user for the number of rows to display and validating the input
    num_rows = get_valid_input()

    # Displaying the sorted data, formatted according to the user's choice
    print("---------------------------------------------------------------------------------------")
    for i in range(num_rows):
        if i < len(sorted_data):
            # Display each row in the specified format
            print(f"{sorted_data[i][0]:<8} {sorted_data[i][1]:<10} {sorted_data[i][2]:<12} "
                  f"{sorted_data[i][3]:<25} {sorted_data[i][4]:<8} {sorted_data[i][5]:<15} "
                  f"{sorted_data[i][6]:<8} {sorted_data[i][7]:<8} ")
    print("---------------------------------------------------------------------------------------")

# Running the program when executed
if __name__ == "__main__":
    main()
