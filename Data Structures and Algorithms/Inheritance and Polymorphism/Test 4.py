# superclass
class Employee:
    def __init__(self, name=None, employee_id=None):
        self.__name = name
        self.__employee_id = employee_id

    def calculate_salary(self):
        pass
    
    def get_info(self):
        return (f"Name: {self.__name} || Employee ID : {self.__employee_id}")

# subclass 1 for Employee
class FullTimeEmployee(Employee):
    def __init__(self, name=None, employee_id=None, base_salary=0.0):
        super().__init__(name, employee_id)
        self.__base_salary = base_salary

    @property
    def base_salary(self):
        return self.__base_salary
    
    def calculate_salary(self):
        return self.__base_salary

    def get_info(self):
        return f"{super().get_info()} || Base Salary : {self.__base_salary}"

# subclass 1 for FullTimeEmployee
class Technical(FullTimeEmployee):
    def __init__(self, name=None, employee_id=None, base_salary=0.0, bonus=0.0):
        super().__init__(name, employee_id, base_salary)
        self.__bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.__bonus

    def get_info(self):
        return f"{super().get_info()} || Bonus : {self.__bonus}"

# subclass 2 for FullTimeEmployee
class Sales(FullTimeEmployee):
    def __init__(self, name=None, employee_id=None, base_salary=0, commission=0.0, sales_amount=0.0):
        super().__init__(name, employee_id, base_salary) 
        self.__commission = commission
        self.__sales_amount = sales_amount

    def calculate_salary(self):
        return self.base_salary + (self.__commission * self.__sales_amount)

    def get_info(self):
        return f"{super().get_info()} || Commission : {self.__commission} || Sales Amount : {self.__sales_amount}"

# subclass 2 for Employee
class SeasonalEmployee(Employee):
    def __init__(self, name=None, employee_id=None, season=None):
        super().__init__(name, employee_id)
        self.__season = season

    def calculate_salary(self):
        pass

    def get_info(self):
        return f"{super().get_info()} || Season : {self.__season}"

# subclass 1 for SeasonEmployee    
class Holiday(SeasonalEmployee):
    def __init__(self, name=None, employee_id=None, season=None, daily_rate=0.0):
        super().__init__(name, employee_id, season)
        self.__daily_rate = daily_rate

    def calculate_salary(self, days_worked):
        return (self.__daily_rate * days_worked)
    
    def get_info(self):
        return f"{super().get_info()} || Daily Rate : {self.__daily_rate}"
    
# subclass 2 for SeasonEmployee
class Summer(SeasonalEmployee):
    def __init__(self, name=None, employee_id=None, season=None, hourly_rate=0.0):
        super().__init__(name, employee_id, season)
        self.__hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked):
        return (self.__hourly_rate * hours_worked)

    def get_info(self):
        return f"{super().get_info()} || Hourly Rate : {self.__hourly_rate}"

# creating an object of each class    
employee = Employee("A", 100)
fulltime = FullTimeEmployee("B", 101, 1)
tech = Technical("C", 102, 2, 2)
sale = Sales("D", 103, 3, 3, 3)
season = SeasonalEmployee("E", 104, "Sunny")
holiday = Holiday("F", 105, "Cloudy", 4)
summer = Summer("G", 106, "Rainy", 5)

people = [employee, fulltime, tech, sale, season]
people2 = [holiday, summer]

# using duck typing in using .get_info() and .calculate_salary()
for i in people:
    print(i.get_info(), end="") 
    print(" || Salary :",i.calculate_salary())

for i in people2:
    print(i.get_info(), end="")
    print(" || Salary :",i.calculate_salary(2))

# sugod diri nga line mao ni ako gi pass ni sir...
# 
# superclass
# class Employee:
#     def __init__(self, name=None, employee_id=None):
#         self.__name = name
#         self.__employee_id = employee_id

#     def calculate_salary(self):
#         pass
    
#     def get_info(self):
#         return (f"Name: {self.__name} || Employee ID : {self.__employee_id}")

# class FullTimeEmployee(Employee):
#     def __init__(self, name=None, employee_id=None, base_salary=0.0):
#         super().__init__(name, employee_id)
#         self.__base_salary = base_salary

#     @property
#     def base_salary(self):
#         return self.__base_salary
    
#     def calculate_salary(self):
#         return self.__base_salary

#     def get_info(self):
#         return f"{super().get_info()} || Base Salary : {self.__base_salary}"

# class Technical(FullTimeEmployee):
#     def __init__(self, name=None, employee_id=None, base_salary=0.0, bonus=0.0):
#         super().__init__(name, employee_id, base_salary)
#         self.__bonus = bonus

#     def calculate_salary(self):
#         return self.base_salary + self.__bonus

#     def get_info(self):
#         return f"{super().get_info()} || Bonus : {self.__bonus}"

# class Sales(FullTimeEmployee):
#     def __init__(self, name=None, employee_id=None, base_salary=0, commission=0.0, sales_amount=0.0):
#         super().__init__(name, employee_id, base_salary) 
#         self.__commission = commission
#         self.__sales_amount = sales_amount

#     def calculate_salary(self):
#         return self.base_salary + (self.__commission * self.__sales_amount)

#     def get_info(self):
#         return f"{super().get_info()} || Commission : {self.__commission} || Sales Amount : {self.__sales_amount}"
    
# class SeasonalEmployee(Employee):
#     def __init__(self, name=None, employee_id=None, season=None):
#         super().__init__(name, employee_id)
#         self.__season = season

#     def calculate_salary(self):
#         pass

#     def get_info(self):
#         return f"{super().get_info()} || Season : {self.__season}"
    
# class Holiday(SeasonalEmployee):
#     def __init__(self, name=None, employee_id=None, season=None, daily_rate=0.0):
#         super().__init__(name, employee_id, season)
#         self.__daily_rate = daily_rate

#     def calculate_salary(self, days_worked):
#         return (self.__daily_rate * days_worked)
    
#     def get_info(self):
#         return f"{super().get_info()} || Daily Rate : {self.__daily_rate}"
    
# class Summer(SeasonalEmployee):
#     def __init__(self, name=None, employee_id=None, season=None, hourly_rate=0.0):
#         super().__init__(name, employee_id, season)
#         self.__hourly_rate = hourly_rate

#     def calculate_salary(self, hours_worked):
#         return (self.__hourly_rate * hours_worked)

#     def get_info(self):
#         return f"{super().get_info()} || Hourly Rate : {self.__hourly_rate}"
    
# employee = Employee("A", 100)
# fulltime = FullTimeEmployee("B", 101, 1)
# tech = Technical("C", 102, 2, 2)
# sale = Sales("D", 103, 3, 3, 3)
# season = SeasonalEmployee("E", 104, "Sunny")
# holiday = Holiday("F", 105, "Cloudy", 4)
# summer = Summer("G", 106, "Rainy", 5)

# people = [employee, fulltime, tech, sale]
# people2 = [season, holiday, summer]

# for i in people:
#     print(i.get_info()) 
# for i in people:
#     print(i.calculate_salary())
# print()
# for i in people2:
#     print(i.get_info())

# print("Salary : ", season.calculate_salary())
# print("Salary : ", holiday.calculate_salary(1))
# print("Salary : ", summer.calculate_salary(2))