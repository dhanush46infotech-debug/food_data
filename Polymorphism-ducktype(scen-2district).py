# Parent class
class District:
    def info(self):
        print("General District Information")


# --- 25 Tamil Nadu District Classes ---

class Chennai(District):
    def info(self):
        print("Chennai: Capital city of Tamil Nadu")

class Coimbatore(District):
    def info(self):
        print("Coimbatore: Manchester of South India")

class Madurai(District):
    def info(self):
        print("Madurai: Meenakshi Amman Temple")

class Trichy(District):
    def info(self):
        print("Trichy: Rockfort Temple")

class Salem(District):
    def info(self):
        print("Salem: Famous for Mangoes")

class Thanjavur(District):
    def info(self):
        print("Thanjavur: Big Temple (Brihadeeswarar)")

class Tirunelveli(District):
    def info(self):
        print("Tirunelveli: Famous for Halwa")

class Kanyakumari(District):
    def info(self):
        print("Kanyakumari: Southern tip of India")

class Vellore(District):
    def info(self):
        print("Vellore: Golden Temple")

class Erode(District):
    def info(self):
        print("Erode: Turmeric City")

class Thoothukudi(District):
    def info(self):
        print("Thoothukudi: Pearl City")

class Dindigul(District):
    def info(self):
        print("Dindigul: Famous for Biriyani")

class Thiruvarur(District):
    def info(self):
        print("Thiruvarur: Temple City")

class Dharmapuri(District):
    def info(self):
        print("Dharmapuri: Mango Capital")

class Krishnagiri(District):
    def info(self):
        print("Krishnagiri: Famous for Hills and Mangoes")

class Villupuram(District):
    def info(self):
        print("Villupuram: Largest District (before split)")

class Kanchipuram(District):
    def info(self):
        print("Kanchipuram: Silk Saree City")

class Namakkal(District):
    def info(self):
        print("Namakkal: Transport Hub")

class Sivaganga(District):
    def info(self):
        print("Sivaganga: Chettinad Cuisine")

class Ramanathapuram(District):
    def info(self):
        print("Ramanathapuram: Rameswaram Temple")

class Pudukkottai(District):
    def info(self):
        print("Pudukkottai: Archeological Sites")

class Cuddalore(District):
    def info(self):
        print("Cuddalore: Silver Beach")

class Nagapattinam(District):
    def info(self):
        print("Nagapattinam: Velankanni Church")

class Ariyalur(District):
    def info(self):
        print("Ariyalur: Cement Factories")

class Karur(District):
    def info(self):
        print("Karur: Textile & Bus Body Building")


# Polymorphism Function
def show_info(district):
    district.info()


# ------------------------------
# Create Objects (25 Districts)
# ------------------------------
districts = [
    District(), Chennai(), Coimbatore(), Madurai(), Trichy(),
    Salem(), Thanjavur(), Tirunelveli(), Kanyakumari(), Vellore(),
    Erode(), Thoothukudi(), Dindigul(), Thiruvarur(), Dharmapuri(),
    Krishnagiri(), Villupuram(), Kanchipuram(), Namakkal(), Sivaganga(),
    Ramanathapuram(), Pudukkottai(), Cuddalore(), Nagapattinam(), Ariyalur(),
    Karur()
]

# ------------------------------
# Call Polymorphic Function
# ------------------------------
for d in districts:
    show_info(d)
