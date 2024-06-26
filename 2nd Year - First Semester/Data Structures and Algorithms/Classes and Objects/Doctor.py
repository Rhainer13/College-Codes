class Doctor:
    
    def __init__(self, doctor_name = None):
        self.__doctor_name = doctor_name
        self.__patient_list = []

    @property
    def doctor_name(self):
        return self.__doctor_name
    
    @doctor_name.setter
    def doctor_name(self,doctor_name):
        self.__doctor_name = doctor_name

    @property
    def patient_list(self):
        return self.__patient_list
    
    @patient_list.setter
    def patient_list(self, patient_list):
        self.__patient_list = patient_list

    def add_patient(self, new_patient = None):
        if new_patient not in self.__patient_list:
            self.__patient_list.append(new_patient)

    def remove_patient(self, patient_to_remove):
        if patient_to_remove in self.__patient_list:
            self.__patient_list.remove(patient_to_remove)

    def display_patient_list(self):
        if self.__patient_list != []:
            return (f"Doctor     : {self.__doctor_name}"
                    f"\nPatients   : {self.__patient_list}")
        else:
            return (f"Doctor     : {self.__doctor_name}"
                    f"\nPatients   : Empty")
    
doc1 = Doctor("Dr. Who")

doc1.add_patient(1)
doc1.add_patient(2)

print(doc1.display_patient_list(), "\n")

doc1.remove_patient(1)

print(doc1.display_patient_list())