class company():
    def __init__(self):
        self.company="google"

class b(company):
    pass
b1=b()
print(b1._company)
