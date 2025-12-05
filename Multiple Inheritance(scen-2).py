# Super class
class Date:
    def __init__(self, date):
        self.date = date


# Super class
class Time:
    def __init__(self, time):
        self.time = time


# Sub class inherits Date and Time
class timestamp(Date, Time):
    def __init__(self, date, time):
        Date.__init__(self, date)     # call Date class constructor
        Time.__init__(self, time)     # call Time class constructor
        DateTime = self.date + ' ' + self.time
        print("\nFinal Timestamp :", DateTime)


# -----------------------------
# Take Input From User
# -----------------------------
print("=== Enter Timestamp Details ===")

date = input("Enter Date (YYYY-MM-DD) : ")
time = input("Enter Time (HH:MM:SS)   : ")

# Create timestamp object
ts = timestamp(date, time)
