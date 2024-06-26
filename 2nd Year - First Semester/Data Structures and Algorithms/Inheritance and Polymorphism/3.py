# Base class
class Employee:
    def __init__(self, name=None, salary=0):
        self.__name = name
        self.__salary = salary
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def info(self):
        return(f"Name     : {self.name}")

    def calculateSalary(self):
        return self.__salary

# subclass 1
class Manager(Employee):
    def __init__(self, name=None, bonus=0, salary=0):
        super().__init__(name, salary)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    # def info(self):
    #     return(f"Name: {self.name}")

    def info(self):
        return super().info()

    def calculateSalary(self):
        return self.salary + self.bonus
    
# subclass 2
class Developer(Employee):
    def __init__(self, name=None, salary=0):
        super().__init__(name, salary)

    # def info(self):
    #     return(f"Name: {self.name}")
    
    def info(self):
        return super().info()

    def calculateSalary(self):
        # base salaray plus 10% bonus
        return self.salary + (self.salary*.1)
    
# subclass 3
class Designer(Employee):
    def __init__(self, name=None, salary=0):
        super().__init__(name, salary)

    # def info(self):
    #     return(f"Name: {self.name}")
    
    def info(self):
        return super().info()

    def calculateSalary(self):
        # base salary plus 8% bonus
        return self.salary + (self.salary*.08)

# for polymorphism
def info(type):
    print(type.info())

# for polymorphism
def calculate(type):
    print("Salary   : $ ", end="")
    print(type.calculateSalary(), "\n")

# driver code/ main code
manager = Manager("Manager", 35_000)
developer = Developer("Developer", 30_000)
designer = Designer("Designer", 25_000)

# using polymorphism
info(manager)
calculate(manager)

info(developer)
calculate(developer)

info(designer)
calculate(designer)