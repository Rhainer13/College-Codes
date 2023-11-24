class Product:
    def __init__(self, productID=None, productName=None, price=0.0):
        self.__productID = productID
        self.__productName = productName
        self.__price = price

    @property
    def productID(self):
        return self.__productID
    
    @productID.setter
    def productID(self, productID):
        self.__productID = productID
    
    @property
    def productName(self):
        return self.__productName

    @productName.setter
    def productName(self, productName):
        self.__productName = productName

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f"ID : {self.__productID} || Name : {self.__productName} || Price : Php {self.__price}"

class Electronics(Product):
    def __init__(self, productID=None, productName=None, price=0, warrantyPeriod=0, brand=None):
        super().__init__(productID, productName, price)
        self.__warrantyPeriod = warrantyPeriod
        self.__brand = brand

    @property
    def warrantyPeriod(self):
        return self.__warrantyPeriod
    
    @warrantyPeriod.setter
    def warrantyPeriod(self, warrantyPeriod):
        self.__warrantyPeriod = warrantyPeriod

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    def __str__(self):
        return f"{super().__str__()} || Warranty Period (Months) : {self.__warrantyPeriod} || Brand : {self.__brand}"

class Clothing(Product):
    def __init__(self, productID=None, productName=None, price=0, size=None, color=None):
        super().__init__(productID, productName, price)
        self.__size = size
        self.__color = color

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    def __str__(self):
        return f"{super().__str__()} || Size : {self.__size} || Color : {self.__color}"

class Books(Product):
    def __init__(self, productID=None, productName=None, price=0, author=None, genre=None):
        super().__init__(productID, productName, price)
        self.__author = author
        self.__genre = genre

    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def __str__(self):
        return f"{super().__str__()} || Author : {self.__author} || Genre : {self.__genre}"

class Cart:
    def __init__(self):
        self.__cart = []

    def add_products(self, product):
        self.__cart.append(product)

    def view_cart(self):
        if self.__cart:
            for product in self.__cart:
                print(f">> {product}")
        else:
            print(">> EMPTY")
            
    def calculate_cost(self):
        return sum(product.price for product in self.__cart)
         
class Customer:
    def __init__(self, name=None):
        self.__cart = Cart()
        self.__name = name
        self.__inventory = None

    def browse_products(self, inventory):
        self.__inventory = inventory
        for product in self.__inventory:
            print(f">> {product}")
    
    def add_products(self, productID=None):
        if productID != None:
            for product in inventory:
                if productID == product.productID:
                    self.__cart.add_products(product)
                    return f"{product.productName} has been Added"
                        
            return(f"{productID} not in the Inventory")
        return "No action"
    
    # def add_products(self, product):
    #     self.__cart.add_products(product)
    
    def view_cart(self):
        self.__cart.view_cart()

    def place_order(self):
        total = self.__cart.calculate_cost()
        if total > 0:
            print("\n================================="
                  f"\nOrder Successful for {self.__name}"
                  f"\nTotal Cost : Php {total}", "\n"
                  "=================================")
        else:
            print(f"\nOrder Unsuccessful for {self.__name}")

product = Product(101, "Apple", 5)
electronic = Electronics(102, "Ipad", 1500, 12, "Apple")
clothing = Clothing(103, "Nike", 100, "L", "Blue")
book = Books(104, "Harry Potter", 50, "J.K Rowling", "Fantasy")

inventory = [product, electronic, clothing, book]

customer = Customer("Rhainer")

print("\n---LIST OF PRODUCTS---")
customer.browse_products(inventory)

print("\n--ACTIONS--")
print(customer.add_products())
print(customer.add_products(101))
# print(customer.add_products(101, inventory))
# print(customer.add_products(100, inventory))
# print(customer.add_products(102, inventory))
# print(customer.add_products(103, inventory))
# print(customer.add_products(104, inventory))

# customer.add_products(product)
# customer.add_products(electronic)
# customer.add_products(electronic)
# customer.add_products(electronic)
# customer.add_products(clothing)
# customer.add_products(book)

print("\n---CUSTOMER CART---")
customer.view_cart()

customer.place_order()