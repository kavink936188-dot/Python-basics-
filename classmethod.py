class laptop:
    chargertype="b-type"

    def __init__(self):
        self.brand=""
        self.price=34

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="C-type"
        print("chargertype changed to c")

    @staticmethod
    def info():
        print("this is laptop class")

hp.laptop()
hp.setprice(2000)
hp.getprice()

laptop.chargertye()

hp.info()
