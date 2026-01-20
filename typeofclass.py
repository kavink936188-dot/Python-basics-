class laptop:
    chargertype="C-type"

    def __init__(self):
        self.brand=""
        self.price="34"

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
        
    @classmethod
    def changechargertype(cls):
        cls.chargertype="b-type"
        print("chargertype changed to B")
        

hp=laptop()
hp.setprice("20000")
hp.getprice()

laptop.changechargertype()

    
