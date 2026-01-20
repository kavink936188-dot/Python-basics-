class laptop:
    def __init__ (self):
        self.ram=""
        self.proccessor=""
    def display(self):
        print("ram:",self.ram)
        print("proccessor:",self.proccessor)

hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.proccessor="i5"
dell.ram="16gb"
dell.proopccessor="i7"

hp.display()
dell.display()
        
