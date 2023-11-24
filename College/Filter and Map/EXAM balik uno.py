# create a list of dictionary
list_of_dictionary = [
    {"Product Name":"Apple","Price": 1, "Rating":1, "In Stock":True},
    {"Product Name":"Apricot","Price": 2, "Rating":1, "In Stock":True},
    {"Product Name":"Avocado","Price": 3, "Rating":2, "In Stock":True},
    {"Product Name":"Banana","Price": 4, "Rating":2, "In Stock":True},
    {"Product Name":"Blueberry","Price": 5, "Rating":3, "In Stock":True},
    {"Product Name":"Blackberry","Price": 6, "Rating":3, "In Stock":False},
    {"Product Name":"Cherry","Price": 7, "Rating":4, "In Stock":False},
    {"Product Name":"Coconut","Price": 8, "Rating":4, "In Stock":False},
    {"Product Name":"Cucumber","Price": 9, "Rating":5, "In Stock":False},
    {"Product Name":"Durian","Price": 10, "Rating":5, "In Stock":False}
]

def filter_by_price(list_of_dictionary):
    return list_of_dictionary["Price"] <= maximum_price

def filter_by_rating(list_of_dictionary):
    return list_of_dictionary["Rating"] >= minimum_rating

def filter_by_availability(list_of_dictionary):
    return list_of_dictionary["In Stock"] == availability

def add_dictionary():
    new_dictionary = {}

    new_dictionary["Product Name"] = input("Product Name\t\t\t: ")
    new_dictionary["Price"] = int(input("Price (1 to 10)\t\t\t: "))
    new_dictionary["Rating"] = int(input("Rating (1 to 5)\t\t\t: "))
    test = input("Availability (True or False)\t: ")
    if test.lower() == "true":
        new_dictionary["In Stock"] = True
    elif test.lower() == "false":
        new_dictionary["In Stock"] = False

    list_of_dictionary.append(new_dictionary)

def show_all():
    for dictionary in list_of_dictionary:
        print(dictionary)

def show_menu():
    print("\n<< MAIN MENU >>\n\n"
          "[1] Add a new product\n"
          "[2] Display all products\n"
          "[3] Filter products by maximum price\n"
          "[4] Filter products by minimum rating\n"
          "[5] Filter products by availability (in stock)\n"
          "[6] Exit the program\n")
    return int(input("Number: "))

# sentinel-controlled loop
while True:
    response = show_menu()
    print()

    if response == 1:
        add_dictionary()
    elif response == 2:
        show_all()
    elif response == 3:
        maximum_price = int(input("Maximum Price : "))
        filtered_price = list(filter(filter_by_price,list_of_dictionary))

        print("\n***FILTERED BY MAXIMUM PRICE***")
        for dictionary in filtered_price:
            print(dictionary)
    elif response == 4:
        minimum_rating = int(input("Minimum Rating (1 to 5): "))
        filtered_rating = list(filter(filter_by_rating,list_of_dictionary))
        
        print("\n***FILTERED BY MINIMUM RATING***")
        for dictionary in filtered_rating:
            print(dictionary)
    elif response == 5:
        test = input("Availability (True or False)\t: ")
        if test.lower() == "true":
            availability = True
        elif test.lower() == "false":
            availability = False
        filtered_availability = list(filter(filter_by_availability,list_of_dictionary))
        
        print("***FILTERED BY AVAILABILITY***")
        for dictionary in filtered_availability:
            print(dictionary)
    elif response == 6:
        print("(Note) You have exited the program...\n")
        break