class grandpa():
    def phone(self):
        print("grandpa phone")

class dad():
    def money(self):
        print("dad's money")

class son(grandpa,dad):
    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()

ram=son()
ram.money()

ram=son()
ram.laptop()
