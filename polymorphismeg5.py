class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salarysalary

class Manager(Employee):
    def __init__(self,department):
        super().__init__(self,name,salary,department)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)

m1=Maneger("CSE")
m1.display()
