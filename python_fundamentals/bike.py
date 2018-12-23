class Bike:

    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("This bikes price is: " + str(self.price) + " dollars")
        print("It's max speed is: " + str(self.max_speed) + " miles per hour")
        if self.miles == 0:
            print("This bike has not been ridden!")
        else:
            print("This bike has " + str(self.miles) + " miles on it!")

    def ride(self):
        print("RIDING!")
        self.miles += 10
        return self 

    def reverse(self):
        print("REVERSING!")
        if self.miles >= 5:
            self.miles -= 5
        else:
            print("Couldn't reverse any further!")
            return self
        return self
    
mountain = Bike(800, 50, 0)
mountain.ride()
mountain.ride()
mountain.ride()
mountain.reverse()
mountain.displayInfo()

bmx = Bike(1200, 20, 0)
bmx.ride()
bmx.ride()
bmx.reverse()
bmx.reverse()
bmx.displayInfo()

roadbike = Bike(1000, 60, 0)
roadbike.reverse()
roadbike.reverse()
roadbike.reverse()
roadbike.displayInfo()