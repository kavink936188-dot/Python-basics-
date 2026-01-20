class goa():
    name="kavin"
    drink=""
    def party(self):
        print("Lets party........")
    def beach(self):
        print("Enjoy the beach")


ramesh=goa()
suresh=goa()

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink="Yes"
suresh.drink="No"


print(ramesh.name)
print("drink:",ramesh.drink)
print(suresh.name)
print("drink:",suresh.drink)

ramesh.party()
suresh.beach()
