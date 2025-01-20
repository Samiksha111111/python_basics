#csv = comma separated values tsv = tab separated values
import csv
import random

#Files name required in this task
sales_data_file = "sales_data.csv"
summary_data_file = "sales_summary.csv"

def create_csv():
    """
    Create a new CSV file with headers
    """
    headers = ["Product", "City", "Quantity", "Price", "Total"]
    with open(sales_data_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Sales summary created.")

#Add a new sale record to the CSV file
def add_sale(product, city, quantity, price):
    total = quantity * price
    with open(sales_data_file, mode ="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product, city, quantity, price, total])
    print("Sale added successfully.")

#Calculate total sales from the CSV file
def calculate_total_sales():
    total_sales = 0 
    with open(sales_data_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_sales += float(row["Total"])
    print(f"Total Sales: ${total_sales:.2f}")

def generate_random_sales_data(num_records):
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

    for _ in range(num_records):
        product = random.choice(products)
        city = random.choice(cities)
        quantity = random.randint(10, 500) #Random units sold
        price = random.uniform(10.0, 1000.0) #Random price
        add_sale(product, city, quantity, price)

    print(f"Generated {num_records} random sales records.")

create_csv() #sales_data_file
generate_random_sales_data(10)