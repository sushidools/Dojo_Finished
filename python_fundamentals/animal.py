class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print("Health is at: " + str(self.health))
        return self

rabbit = Animal("Bugs Bunny", 120)
rabbit.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name, 150) 

    def pet(self):
        self.health += 5
        return self

dogger = Dog("Boo Boo")
#dogger.fly().displayHealth() this does not run
dogger.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170) 

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print("I am a dragon! My health is: " + str(self.health))

dragon1 = Dragon("Toothless")
#dragon1.pet().displayHealth() was recognized to not run
dragon1.fly().displayHealth()
