# Parent Class
class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def PersonInfo(self):
        print('Name   :- {}'.format(self.name))
        print('Age    :- {}'.format(self.age))
        print('Gender :- {}'.format(self.gender))


# Child Class "student"
class student(person):
    def __init__(self, name, age, gender, studentid, fees):
        # calling parent constructor
        person.__init__(self, name, age, gender)
        self.studentid = studentid
        self.fees = fees

    def StudentInfo(self):
        print('Student ID :- {}'.format(self.studentid))
        print('Fees       :- {}'.format(self.fees))


# ------------------------------
# MAIN PROGRAM
# ------------------------------

print("\n--- Enter Student Details ---\n")

name = input("Enter Name        : ")
age = input("Enter Age         : ")
gender = input("Enter Gender      : ")
studentid = input("Enter Student ID  : ")
fees = input("Enter Fees        : ")

# Creating student object
stu = student(name, age, gender, studentid, fees)

print("\n--- STUDENT FULL INFORMATION ---\n")

# Showing details
stu.PersonInfo()
stu.StudentInfo()
