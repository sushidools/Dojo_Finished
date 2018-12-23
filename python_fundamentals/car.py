spc = "\n"
class Car:

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def displayInfo(self):
        print("Price: " + str(self.price))
        print("Speed: " + str(self.speed) + "mph")
        print("Fuel: " + self.fuel)
        print("Mileage: " + str(self.mileage) + "mpg")
        print("Tax: " + str(self.tax))

bmw = Car(10000, 40, 'Full', 30)
bmw.displayInfo()

print(spc)

ford = Car(2000, 35, 'Full', 15)
ford.displayInfo()

print(spc)

nissan = Car(35000, 60, 'Kind of Full', 90)
nissan.displayInfo()

print(spc)

vw = Car(9000, 0, 'Empty', 30)
vw.displayInfo()

print(spc)

tesla = Car(100000, 180, 'Always Full', 100)
tesla.displayInfo()

print(spc)

mercedes = Car(50000, 90, 'Not Full', 70)
mercedes.displayInfo()