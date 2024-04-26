class Teacher:
    def __init__(self, teacher_name = str, subject = str, students = []):
        self.__teacher_name = teacher_name
        self.__subject = subject
        self.__students = students

    def add_student(self, new_student: str):
        if new_student not in self.__students:
            return self.__students.append(new_student)
    
    def remove_student(self, student_to_remove):
        if student_to_remove in self.__students:
            return self.__students.remove(student_to_remove)
        else:
            return(f"{student_to_remove} is not in the class")
        
    def list_students(self):
        return (f"Teacher               : {self.__teacher_name}"
                f"\nSubject               : {self.__subject}"
                f"\nStudents              : {self.__students}")
    
    def student_count(self):
        return (f"Number of Students    : {len(self.__students)}")

teacher1 = Teacher("Sir Tirol", "BSIT II-1")

print("\t\t--BEFORE--")
teacher1.add_student("Rhainer")
teacher1.add_student("Mata")

print(teacher1.list_students())
print(teacher1.student_count(), "\n")

teacher1.remove_student("Rhainer")

print("\t\t--AFTER--")
print(teacher1.list_students())
print(teacher1.student_count())