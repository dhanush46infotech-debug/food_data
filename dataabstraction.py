# Data Abstraction Example – 5 Tamil Nadu Districts

class District:

    def __init__(self, name):
        self.name = name        # Public
        self.famous_for = self.__get_famous_data(name)   # Uses private method

    # -------------------------
    # PRIVATE METHOD (Hidden)
    # -------------------------
    def __get_famous_data(self, district_name):
        """This method is hidden from the user (Abstraction)."""

        data = {
            "Chennai": "IT Hub of Tamil Nadu",
            "Madurai": "Meenakshi Amman Temple",
            "Coimbatore": "Textile Industries",
            "Tirunelveli": "Halwa",
            "Kanyakumari": "Sunrise & Sunset Point"
        }

        return data.get(district_name, "No data available")

    # -------------------------
    # PUBLIC METHOD (Visible)
    # -------------------------
    def show_details(self):
        print(f"District: {self.name}")
        print(f"Famous For: {self.famous_for}")
