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

#print("\nFILTERED BY PRICE (less than or equal to FIVE)")
def filter_price(dictionary):
    return dictionary["Price"] <= maximum_price

#print("\nFILTERED BY RATING (less than or equal to FOUR)")
def filter_rating(dictionary):
    return dictionary["Rating"] >= minimum_rating

#print("\nFILTERED BY AVAILABILITY (True)")
def filter_availability(dictionary):
    return dictionary["In Stock"] == True

while True:
    new_dictionary = {}

    print("\n[1] Add a new product\n"
          "[2] Display all products\n"
          "[3] Filter products by maximum price\n"
          "[4] Filter products by minimum rating\n"
          "[5] Filter products by availability (in stock)\n"
          "[6] Exit the program\n")

    response = int(input("RESPONSE: "))
    print()

    if response == 6:
        break
    elif response == 1:
        product_name = input(">> Product Name\t\t\t: ")
        new_dictionary["Product Name"] = product_name

        price = int(input(">> Price\t\t\t: "))
        new_dictionary["Price"] = price

        rating = int(input(">> Rating\t\t\t: "))
        new_dictionary["Rating"] = rating

        in_stock = bool(input(">> In Stock (True or False)\t: "))
        new_dictionary["In Stock"] = in_stock
        
        list_of_dictionary.append(new_dictionary)

    elif response == 2:
        for dictionary in list_of_dictionary:
            print(dictionary)

    elif response == 3:
        maximum_price = int(input("Maximum Price to Filter: "))

        #filtered_price = list(filter(filter_price,list_of_dictionary))
        filtered_price = list(filter(lambda dictionary: int(dictionary["Price"]) <= maximum_price, list_of_dictionary))

        for dictionary in filtered_price:
            print(dictionary)

    elif response == 4:
        minimum_rating = int(input("Minimum Rate to Filter: "))

        filtered_rating = list(filter(lambda dictionary:int(dictionary["Rating"]) >= minimum_rating, list_of_dictionary))
        #filtered_rating = list(filter(filter_rating,list_of_dictionary))

        for dictionary in filtered_rating:
            print(dictionary)
    
    elif response == 5:
        #filtered_availability = list(filter(lambda dictionary:dictionary["In Stock"] == True, list_of_dictionary))
        filtered_availability = list(filter(filter_availability,list_of_dictionary))

        for dictionary in filtered_availability:
            print(dictionary)

    elif response == 6:
        print("Thank you")
        break