# Data Encapsulation Example with 5 Tamil Nadu Districts

class District:
    def __init__(self, name, famous_for):
        # Private attributes (encapsulated)
        self.__name = name
        self.__famous_for = famous_for

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, new_name):
        self.__name = new_name

    # Getter method for famous_for
    def get_famous_for(self):
        return self.__famous_for

    # Setter method for famous_for
    def set_famous_for(self, new_info):
        self.__famous_for = new_info

    # Display method
    def show_details(self):
        print(f"District: {self.__name}")
        print(f"Famous For: {self.__famous_for}")


# --------------------------
# Create 5 District Objects
# --------------------------

d1 = District("Chennai", "Marina Beach")
d2 = District("Madurai", "Meenakshi Amman Temple")
d3 = District("Coimbatore", "Textile Industries")
d4 = District("Tirunelveli", "Halwa")
d5 = District("Kanyakumari", "Sunrise & Sunset Point")

# --------------------------
# Show details (Encapsulated data)
# --------------------------
d1.show_details()
d2.show_details()
d3.show_details()
d4.show_details()
d5.show_details()

# --------------------------
# Updating data using setter (Encapsulation)
# --------------------------
d3.set_famous_for("Textile Hub of Tamil Nadu")

print("After Updating Famous For (Using Setter):")
d3.show_details()

