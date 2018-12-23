class Animal(object):
    def __init__(self, name, health):
        self.name = name 
        self.health = health 

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

animal1 = Animal("Fido", 100)
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
        
    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Jake")
dog1.walk().walk().walk().run().run().pet().display_health()

class Animal(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def displayHealth(self):
        print self.health
        return self

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self


rabbit = Animal("Bugs Bunny", 120)
rabbit.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name, 150)

    def pet(self):
        self.health += 5
        return self

dogger = Dog("Boo Boo", health)
dogger.walk().walk().walk().run().run().pet().displayHealth()

    
class Dragon(Animal):

    def __init__(self, name, health):
        super(Dragon, self).__init__(name, 170)

    def displayHealth(self):
        print("I am a dragon!")

    def fly(self):
        self.health -= 10
        return self


dragon1 = Dragon("Austin")
