class student:
    def __init__(self):
        self.name="kavin"
        self.regno="12345"
    def display(self):
        print("Name",self.name)
        print("Reg No",self.regno)

s1=student()
s2=student()

s1.name="manoj"
s1.regno="1"

s2.name="karthi"
s2.regno="2"

s1.display()
s2.display()
    
    
