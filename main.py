class Device:
    def __init__(self, name):
        self.name = name
        self.status = False

    def on(self):
        self.status = True

    def off(self):
        self.status = False

class SmartHome:
    def __init__(self):
        self.devices = []

    def add(self, name):
        self.devices.append(Device(name))

    def control(self, name, state):
        for d in self.devices:
            if d.name == name:
                d.on() if state else d.off()

    def show(self):
        for d in self.devices:
            print(d.name, "ON" if d.status else "OFF")

def run():
    home = SmartHome()
    home.add("Lamp")
    home.add("TV")

    while True:
        print("\n1. Qurilmalar\n2. Yoq/O‘ch\n3. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            home.show()
        elif c == "2":
            home.control(input("Nomi: "), input("1-ON, 0-OFF: ")=="1")
        else:
            break

run()
