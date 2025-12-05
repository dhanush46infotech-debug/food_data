# Duck-typing example: no inheritance required

class PersonLike:
    def __init__(self, name):
        self.name = name
    def summary(self):
        print(f"PersonLike: {self.name}")

class EmployeeLike:
    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
    def summary(self):
        # different internal structure, same method name
        print(f"EmployeeLike: {self.name}, ID: {self.empid}")

class FullTimeLike:
    def __init__(self, name, years):
        self.name = name
        self.years = years
    def summary(self):
        print(f"FullTimeLike: {self.name}, Exp: {self.years}")

# function uses duck typing: it just calls summary()
def print_summary(obj):
    # as long as obj has summary(), this works
    obj.summary()

print("\n=== Duck typing demo ===")
print_summary(PersonLike("Meena"))
print_summary(EmployeeLike("Arun", "E101"))
print_summary(FullTimeLike("Dhanush", "5 years"))
