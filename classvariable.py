class phone:
    chargertype="B-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargertype:",self.chargertype)

phone.chargertype="C-TYPE"

samsung=phone("SAMSUNG","100000")
samsung.display()

google=phone("pixel","150000")
google.display()

iphone=phone("IPHONE","100000")
iphone.display()

vivo=phone("VIVO","15000")
vivo.display()

oppo=phone("OPPO","12000")
oppo.display()

redmi=phone("REDMI","50000")
redmi.display()

               

               
    
