class Teacher:
    def __init__ (self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name",self.name)
        print("Reg No",self.regno)

t1=Teacher("kavin","1")
t2=Teacher("jhon","2")

t1.display()
t2.display()
