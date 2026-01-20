class vehicle():
    def start(self):
        print("start the vehicle")

class car(vehicle):
    def __init__(self):
        print("car started")

v1=vehicle()
v1.start()

c1=car()
c1.start()
