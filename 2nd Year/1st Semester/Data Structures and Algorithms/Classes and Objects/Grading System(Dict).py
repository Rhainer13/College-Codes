import statistics

class Teacher:
    def __init__(self, teacher_name = None, subject = None):
        self.__teacher_name = teacher_name
        self.__subject = subject
        self.__students_info = {}

    def add_student(self, student_name, grade):
        self.__students_info[student_name] = grade

    def remove_student(self, student_name):
        del self.__students_info[student_name]

    def get_grade(self, student_name):
        return self.__students_info[student_name]
    
    def average_grade(self):
        total_grades = sum(grade for grade in self.__students_info.values())
        average = total_grades/len(self.__students_info)
        return average 
    
    def highest_grade(self):
        highest = max(self.__students_info.values())
        return (f"Highest Grade                 : {highest}")
    
    def lowest_grade(self):
        lowest = min(self.__students_info.values())
        return (f"Lowest Grade                  : {lowest}")

    def list_of_students(self):
        if self.__students_info != {}:
            for student, grade in self.__students_info.items():
                print(f"Student : {student}"
                    f"\nGrade   : {grade}")
        
t1 = Teacher("Sir Tirol", "Programming")
print()
t1.add_student("a",1)
t1.add_student("b",2)
t1.list_of_students()
print()
t1.remove_student("a")
t1.list_of_students()
print()
print(t1.average_grade())
print(t1.highest_grade())
print(t1.lowest_grade())