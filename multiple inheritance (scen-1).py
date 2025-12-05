# Super Class
class Father:
    def __init__(self, fathername):
        self.fathername = fathername


# Super Class
class Mother:
    def __init__(self, mothername):
        self.mothername = mothername


# Sub Class inherits both Father and Mother super classes
class Son(Father, Mother):
    def __init__(self, fathername, mothername, name):
        Father.__init__(self, fathername)     # calling Father constructor
        Mother.__init__(self, mothername)     # calling Mother constructor
        self.name = name

    def show(self):
        print("\n--- FAMILY DETAILS ---")
        print("My Name   :-", self.name)
        print("Father    :-", self.fathername)
        print("Mother    :-", self.mothername)


# ----------------------------
# Taking Input From User
# ----------------------------

fathername = input("Enter Father's Name : ")
mothername = input("Enter Mother's Name : ")
name       = input("Enter your Name : ")

# Creating object
s = Son(fathername, mothername, name)

# Displaying details
s.show()
