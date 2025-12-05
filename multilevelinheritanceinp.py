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


# Child Class
class employee(person):
    def __init__(self, name, age, gender, empid, salary):
        person.__init__(self, name, age, gender)   # calling parent constructor
        self.empid = empid
        self.salary = salary

    def employeeInfo(self):
        print('Employee ID :- {}'.format(self.empid))
        print('Salary      :- {}'.format(self.salary))
    # Grandchild class 1 (full-time employee)
class fulltime(employee):
    def __init__(self, name, age, gender, empid, salary, WorkExperience):
        super().__init__(name, age, gender, empid, salary)   # init employee (and person)
        # alternatively: employee.__init__(self, name, age, gender, empid, salary)
        self.WorkExperience = WorkExperience

    def FulltimeInfo(self):
        print('Work Experience :- {}'.format(self.WorkExperience))


# Grandchild class 2 (contractual employee)
class contractual(employee):
    def __init__(self, name, age, gender, empid, salary, ContractExpiry):
        super().__init__(name, age, gender, empid, salary)
        # alternatively: employee.__init__(self, name, age, gender, empid, salary)
        self.ContractExpiry = ContractExpiry

    def ContractInfo(self):
        print('Contract Expiry :- {}'.format(self.ContractExpiry))


# -------------------------
# Demo: create objects and show all details
# -------------------------
if __name__ == "__main__":
    # Fulltime employee example
    ft = fulltime("Dhanush", 24, "Male", "FT001", 55000, "5 years")
    print("Fulltime Employee Details:")
    ft.PersonInfo()
    ft.employeeInfo()
    ft.FulltimeInfo()
    print("-" * 50)

    # Contractual employee example
    ct = contractual("DK", 25, "Male", "CT101", 30000, "2026-06-30")
    print("Contractual Employee Details:")
    ct.PersonInfo()
    ct.employeeInfo()
    ct.ContractInfo()
    print("-" * 50)