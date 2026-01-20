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
    def ChangeChargerType(cls):
        cls.chargertype="B-type"
        print("charger type changed to B")

    @staticmethod
    def info():
        print("this is laptop class")

hp=laptop()
hp.setprice(2000)
hp.getprice()

laptop.ChangeChargerType()

hp.info()
