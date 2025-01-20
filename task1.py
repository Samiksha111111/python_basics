import csv

def parse_csv_for_totals(file_path):
    row_totals = {}       # Dictionary to store total of each row
    column_totals = {}    # Dictionary to store total of each column

    # Open the CSV file in read mode
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)   # Create a CSV reader object
        headers = next(reader)      # Read the first row as headers

        # Initialize column totals with zero for each header (excluding the first one)
        for header in headers[1:]:
            column_totals[header] = 0

        # Iterate through each row in the CSV file
        for row in reader:
            category = row[0]                           # The first value in each row is the category
            values = list(map(int, row[1:]))            # Convert the rest of the row values to integers
            row_totals[category] = sum(values)          # Calculate the sum of the row values and store in row_totals

            # Update column totals
            for header, value in zip(headers[1:], values):
                column_totals[header] += value          # Add the current row's value to the corresponding column total

    # Output the row totals
    print("Row Totals:")
    for category, total in row_totals.items():
        print(f"{category}: {total}")

    # Output the column totals
    print("\nColumn Totals:")
    for header, total in column_totals.items():
        print(f"{header}: {total}")

# File path to the CSV file
file_path = 'data.csv'

# Call the function to parse the CSV and calculate totals
parse_csv_for_totals(file_path)
