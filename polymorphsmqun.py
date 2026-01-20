class Animal():
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class bird(Animal):
    def sound(self):
        print("Birds sing")
    

A1=Animal()
A1.sound()

D1=Dog()
D1.sound()

B1=bird()
B1.sound()
