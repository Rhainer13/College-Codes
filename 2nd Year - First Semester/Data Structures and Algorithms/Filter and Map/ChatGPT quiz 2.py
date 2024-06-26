# Initial list of products
products = [
    {"Product Name": "Laptop", "Price": 999.99, "Rating": 4.5, "In Stock": True},
    {"Product Name": "Smartphone", "Price": 499.99, "Rating": 4.2, "In Stock": True},
    {"Product Name": "Headphones", "Price": 79.99, "Rating": 4.0, "In Stock": False},
    {"Product Name": "Camera", "Price": 599.99, "Rating": 4.7, "In Stock": True},
    {"Product Name": "Tablet", "Price": 299.99, "Rating": 4.3, "In Stock": False},
    {"Product Name": "Monitor", "Price": 349.99, "Rating": 4.6, "In Stock": True},
    {"Product Name": "Keyboard", "Price": 49.99, "Rating": 4.1, "In Stock": True},
    {"Product Name": "Mouse", "Price": 19.99, "Rating": 3.9, "In Stock": True},
    {"Product Name": "Printer", "Price": 129.99, "Rating": 4.4, "In Stock": False},
    {"Product Name": "External Hard Drive", "Price": 89.99, "Rating": 4.2, "In Stock": True},
]

# Function to add a new product to the list
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    rating = float(input("Enter product rating (1-5): "))
    in_stock = input("Is the product in stock (True/False): ").capitalize() == "True"
    
    new_product = {
        "Product Name": name,
        "Price": price,
        "Rating": rating,
        "In Stock": in_stock
    }
    
    products.append(new_product)
    print("Product added successfully!")

# Function to filter products by maximum price
def filter_by_price(max_price):
    filtered_products = [product for product in products if product["Price"] <= max_price]
    return filtered_products

# Function to filter products by minimum rating
def filter_by_rating(min_rating):
    filtered_products = [product for product in products if product["Rating"] >= min_rating]
    return filtered_products

# Function to filter products by availability (in stock)
def filter_by_availability():
    filtered_products = [product for product in products if product["In Stock"]]
    return filtered_products

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Add a new product")
    print("2. Display all products")
    print("3. Filter products by maximum price")
    print("4. Filter products by minimum rating")
    print("5. Filter products by availability (in stock)")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        print("\nAll Products:")
        for product in products:
            print(product)
    elif choice == "3":
        max_price = float(input("Enter maximum price: "))
        filtered = filter_by_price(max_price)
        print("\nProducts with price less than or equal to", max_price, ":")
        for product in filtered:
            print(product)
    elif choice == "4":
        min_rating = float(input("Enter minimum rating (1-5): "))
        filtered = filter_by_rating(min_rating)
        print("\nProducts with rating greater than or equal to", min_rating, ":")
        for product in filtered:
            print(product)
    elif choice == "5":
        filtered = filter_by_availability()
        print("\nProducts currently in stock:")
        for product in filtered:
            print(product)
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")