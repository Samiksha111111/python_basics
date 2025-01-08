import csv
#files path for csv tracker
file_path="Sales_tracker.csv"
#create a new csv files with reader
def create_csv():
    headers=["Date", "Product", "Quantity", "Price per unit", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created")

#add new ssles record to the csv file
def add_sales(date,product,quantity, price_per_unit):
    total=quantity*price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("Sales record added")

#Calculate total sales from csv file
def calculate_total_sale():
    total_sales=0
    with open(file_path, mode="r", newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            total_sales+=float(row["Total"])
    print(f"Total sales: ${total_sales:.2f}")

#Example usage
create_csv()
add_sales("2025-01-06", "laptop", 2, 1200.50)
add_sales("2025-01-06", "Mouse", 2, 1200.50)
calculate_total_sale()

