class granpa():
    def phone(self):
        print("granpa phone")

class dad(granpa):
    def money(self):
        print("dad's money")

class son(dad,granpa):
    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()
d1=dad()
dad.phone()
