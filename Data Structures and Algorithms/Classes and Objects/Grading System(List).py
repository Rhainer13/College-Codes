import statistics

class Teacher:
    def __init__(self, teacher_name = None, subject = None):
        self.__teacher_name = teacher_name
        self.__subject = subject
        self.__student_info = []

    def add(self, student_name, grade):
        for student in self.__student_info:
            if student['name'] == student_name:
                return(f"(!) {student_name} is already in the list")

        new = {"name":student_name, "grade":grade}
        self.__student_info.append(new)
        return(f"(!) {student_name} is added to the list")
    
    def remove(self, student_name):
        for student in self.__student_info:
            if student['name'] == student_name:
                self.__student_info.remove(student)
                return(f"(!) {student_name} is removed")

        return(f"(!) {student_name} is not in the list")
    
    def get(self, student_name):
        for student in self.__student_info:
            if student_name == student['name']:
                return(f"(!) Requsted Student: {student}")
            
        return(f"(!) {student_name} not in the list")
    
    def highest(self):
        high = self.__student_info[0]
        for student in self.__student_info:
            if student['grade'] > high['grade']:
                high = student
        
        return(f"Highest: {high}")    
    
    def lowest(self):
        return min(student['grade'] for student in self.__student_info)
    
    def average(self):
        total = [student['grade'] for student in self.__student_info]
        return(f"Average Grade of the class: {statistics.mean(total)}")
    
    # def 
    
    def display(self):
        for student in self.__student_info:
            print(student)

t = Teacher("Tirol", "Programming")

print(t.add("A",1))
print(t.add("b",2))
print(t.get("b"))
print(t.highest())
print(t.lowest())
print(t.average(), "\n")

print(t.remove("A"),"\n")

print("LIST OF STUDENTS")
t.display()
print(t.average())