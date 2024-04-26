# superclass
class Product:
    def __init__(self, product_id=None, name=None, description=None, price=None):
        self.__product_id = product_id
        self.__name = name
        self.__description = description
        self.__price = price

    # getter
    @property
    def product_id(self):
        return self.__product_id
    
    # setter
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id

    # getter
    @property
    def name(self):
        return self.__name
    
    # setter
    @name.setter
    def name(self, name):
        self.__name = name

    # getter
    @property
    def description(self):
        return self.__description
    
    # setter
    @description.setter
    def description(self, description):
        self.__description = description

    # getter
    @property
    def price(self):
        return self.__price
    
    # setter
    @price.setter
    def price(self, price):
        self.__price = price

    def get_info(self):
        return f"Product ID : {self.__product_id} || Name : {self.__name} || Description : {self.__description} || Price : Php {self.__price}"

# subclass 1 for Product Class
class Electronics(Product):
    def __init__(self, product_id=None, name=None, description=None, price=None, brand=None, model=None, warranty_period=None, power_consumption=None):
        super().__init__(product_id, name, description, price)
        self.__brand = brand
        self.__model = model
        self.__warranty_period = warranty_period
        self.__power_consumption = power_consumption

    # getter
    @property
    def brand(self):
        return self.__brand
    
    # setter
    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    # getter
    @property
    def model(self):
        return self.__model
    
    # setter
    @model.setter
    def model(self, model):
        self.__model = model

    # getter
    @property
    def warranty_period(self):
        return self.__warranty_period
    
    # setter
    @warranty_period.setter
    def warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period

    # getter
    @property
    def power_consumption(self):
        return self.__power_consumption
    
    # setter
    @power_consumption.setter
    def power_consumption(self, power_consumption):
        self.__power_consumption = power_consumption

    def get_info(self):
        return f"{super().get_info()} || Brand : {self.__brand} || Model : {self.__model} || Warranty Period : {self.__warranty_period} Months || Power Consumption : {self.__power_consumption} watts"

# subclass 1 for Electronics Class
class Smartphone(Electronics):
    def __init__(self, product_id=None, name=None, description=None, price=None, brand=None, model=None, warranty_period=None, power_consumption=None, screen_size=None, camera_resolution=None):
        super().__init__(product_id, name, description, price, brand, model, warranty_period, power_consumption)
        self.__screen_size = screen_size
        self.__camera_resolution = camera_resolution

        # getter
    @property
    def screen_size(self):
        return self.__screen_size
    
    # setter
    @screen_size.setter
    def screen_size(self, screen_size):
        self.__screen_size = screen_size

    # getter
    @property
    def camera_resolution(self):
        return self.__camera_resolution
    
    # setter
    @camera_resolution.setter
    def camera_resolution(self, camera_resolution):
        self.__camera_resolution = camera_resolution

    def get_info(self):
        return f"{super().get_info()} || Screen Size : {self.__screen_size} Inches || Camera Resolution : {self.__camera_resolution} Megapixels"
    
# subclass 2 for Electronics Class
class Laptop(Electronics):
    def __init__(self, product_id=None, name=None, description=None, price=None, brand=None, model=None, warranty_period=None, power_consumption=None, screen_size=None, RAM=None):
        super().__init__(product_id, name, description, price, brand, model, warranty_period, power_consumption)
        self.__screen_size = screen_size
        self.__RAM = RAM

    # getter
    @property
    def screen_size(self):
        return self.__screen_size
    
    # setter
    @screen_size.setter
    def screen_size(self, screen_size):
        self.__screen_size = screen_size

    # getter
    @property
    def RAM(self):
        return self.__RAM
    
    # setter
    @RAM.setter
    def RAM(self, RAM):
        self.__RAM = RAM

    def get_info(self):
        return f"{super().get_info()} || Screen Size : {self.__screen_size} || RAM : {self.__RAM} gb"

# subclass 2 for Product Class
class Clothing(Product):
    def __init__(self, product_id=None, name=None, description=None, price=None, size=None, color=None, material=None):
        super().__init__(product_id, name, description, price)
        self.__size = size
        self.__color = color
        self.__material = material

    # getter
    @property
    def size(self):
        return self.__size
    
    # setter
    @size.setter
    def size(self, size):
        self.__size = size

    # getter
    @property
    def color(self):
        return self.__color
    
    # setter
    @color.setter
    def color(self, color):
        self.__color = color

    # getter
    @property
    def material(self):
        return self.__material
    
    # setter
    @material.setter
    def material(self, material):
        self.__material = material

    def get_info(self):
        return f"{super().get_info()} || Size : {self.__size} || Color : {self.__color} || Material : {self.__material}"

# subclass 1 for Clothing Class
class Shirt(Clothing):
    def __init__(self, product_id=None, name=None, description=None, price=None, size=None, color=None, material=None, sleeve_length=None, collar_size=None):
        super().__init__(product_id, name, description, price, size, color, material)
        self.__sleeve_length = sleeve_length
        self.__collar_size = collar_size

    # getter
    @property
    def sleeve_length(self):
        return self.__sleeve_length
    
    # setter
    @sleeve_length.setter
    def sleeve_length(self, sleeve_length):
        self.__sleeve_length = sleeve_length

    # getter
    @property
    def collar_size(self):
        return self.__collar_size
    
    # setter
    @collar_size.setter
    def collar_size(self, collar_size):
        self.__collar_size = collar_size

    def get_info(self):
        return f"{super().get_info()} || Sleeve Length : {self.__sleeve_length} Inches || Collar Size : {self.__collar_size} Inches"
    
# subclass 2 for Clothing Class
class Jeans(Clothing):
    def __init__(self, product_id=None, name=None, description=None, price=None, size=None, color=None, material=None, waist_size=None, inseam_length=None):
        super().__init__(product_id, name, description, price, size, color, material)
        self.__waist_size = waist_size
        self.__inseam_length = inseam_length

    # getter
    @property
    def waist_size(self):
        return self.__waist_size
    
    # setter
    @waist_size.setter
    def waist_size(self, waist_size):
        self.__waist_size = waist_size

    # getter
    @property
    def inseam_length(self):
        return self.__inseam_length
    
    # setter
    @inseam_length.setter
    def inseam_length(self, inseam_length):
        self.__inseam_length = inseam_length

    def get_info(self):
        return f"{super().get_info()} || Waist Size : {self.__waist_size} Inches || InSeam Length : {self.__inseam_length} Inches"

# subclass 3 for Product Class
class Food(Product):
    def __init__(self, product_id=None, name=None, description=None, price=None, expiry_date=None, calories_per_serving=None, ingredients=[]):
        super().__init__(product_id, name, description, price)
        self.__expiry_date = expiry_date
        self.__calories_per_serving = calories_per_serving
        self.__ingredients = ingredients

    # getter
    @property
    def expiry_date(self):
        return self.__expiry_date
    
    # setter
    @expiry_date.setter
    def expiry_date(self, expiry_date):
        self.__expiry_date = expiry_date

    # getter
    @property
    def calories_per_serving(self):
        return self.__calories_per_serving
    
    # setter
    @calories_per_serving.setter
    def calories_per_serving(self, calories_per_serving):
        self.__calories_per_serving = calories_per_serving

    # getter
    @property
    def ingredients(self):
        return self.__ingredients
    
    # setter
    @ingredients.setter
    def ingredients(self, ingredients):
        self.__ingredients = ingredients

    def get_info(self):
        return f"{super().get_info()} || Expiry Date : {self.__expiry_date} || Calories per Serving : {self.__calories_per_serving} grams || Ingredients : {self.__ingredients}"

# subclass 1 for Food Class
class Fruit(Food):
    def __init__(self, product_id=None, name=None, description=None, price=None, expiry_date=None, calories_per_serving=None, ingredients=[], vitamin_c_content=None, taste=None):
        super().__init__(product_id, name, description, price, expiry_date, calories_per_serving, ingredients)
        self.__vitamin_c_content = vitamin_c_content
        self.__taste = taste

    # getter
    @property
    def vitamin_c_content(self):
        return self.__vitamin_c_content
    
    # setter
    @vitamin_c_content.setter
    def vitamin_c_content(self, vitamin_c_content):
        self.__vitamin_c_content = vitamin_c_content

    # getter
    @property
    def taste(self):
        return self.__taste
    
    # setter
    @taste.setter
    def taste(self, taste):
        self.__taste = taste

    def get_info(self):
        return f"{super().get_info()} || Vitamin C Content : {self.__vitamin_c_content} % || Taste : {self.__taste}"
    
# subclass 2 for Food Class
class DairyProduct(Food):
    def __init__(self, product_id=None, name=None, description=None, price=None, expiry_date=None, calories_per_serving=None, ingredients=[], fat_content=None, type=None):
        super().__init__(product_id, name, description, price, expiry_date, calories_per_serving, ingredients)
        self.__fat_content = fat_content
        self.__type = type

    # getter
    @property
    def fat_content(self):
        return self.__fat_content
    
    # setter
    @fat_content.setter
    def fat_content(self, fat_content):
        self.__fat_content = fat_content

    # getter
    @property
    def type(self):
        return self.__type
    
    # setter
    @type.setter
    def type(self, type):
        self.__type = type

    def get_info(self):
        return f"{super().get_info()} || Fat Content : {self.__fat_content} % || Type : {self.__type}"


# Making an object for each class and subclasses
product = Product(101, "Product", "Sample Product", 5)
electronic = Electronics(102, "Electronic", "To watch Videos", 1500, "Apple", "Gen 3", 12, 65)
smartphone = Smartphone(103, "Smartphone", "For Entertainment", 100, "Samsung", "Galaxy S3", 36, 25, "6.5", "14")
laptop = Laptop(104, "Laptop", "For Work", 35_000, "ASUS", "Vivobook", 12, 65, "1280x720", 8)
clothe = Clothing(105, "Clothe", "Unisex", 10, "Large", "Blue", "Silk")
shirt = Shirt(106, "Shirt", "For Men", 10, "Large", "Blue", "Silk", 10, 10)
jeans = Jeans(107, "Jeans", "For Men", 10, "Medium", "Navy Blue", "Denim", 25, 35)
food = Food(108, "Food", "For Nutrition", 5, "January 1, 2023", 5, ["Apple", "Pie"])
fruit = Fruit(109, "Fruit Salad", "Snacks", 5, "January 2, 2023", 5, ["Apple, Banana"], 10, "Sweet")
dairy = DairyProduct(110, "Dairy Product", "For Bone Strength", 3, "January 3, 2023", 10, ["Fresh Milk", "Butter", "Sugar"], 10, "White Milk")


# printing the information for each object created
print("\n<< LIST OF PRODUCTS >>")
print("-",product.get_info())
print("-",electronic.get_info())
print("-",smartphone.get_info())
print("-",laptop.get_info())
print("-",clothe.get_info())
print("-",shirt.get_info())
print("-",jeans.get_info())
print("-",food.get_info())
print("-",fruit.get_info())
print("-",dairy.get_info())


# gathering all the objects/products to a list/inventory 
inventory = [product, electronic, smartphone, laptop, clothe, shirt, jeans, food, fruit, dairy]

# using polymorphism to display the information of each product
print("\n<< POLYMORPHISM >>")
def get_info(inventory):
    for item in inventory:
        print("+",item.get_info())

get_info(inventory)
print()