class phone:
    chargertype="C-TYPE"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype:",self.chargertype)

samsung = phone("SAMSUNG","20000")
samsung.display()

redme=phone("redme","5000")
redme.display()
