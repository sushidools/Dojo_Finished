spc = "\n"
class Product:

    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def displayInfo(self):
        print("Price: " + str(self.price) + " dollars")
        print("Item: " + self.item_name)
        print("Weight: " + str(self.weight) + " lbs")
        print("Brand: " + self.brand)
        print("Status: " + self.status)

    def sell(self):
        self.status = "sold"
        return self

    def tax(self, x):
        self.price = (self.price * (x)) + self.price
        return self
    
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if reason_for_return == "like_new":
            return self
        if reason_for_return == "opened":
            self.status = "used"
            self.price = self.price - (self.price * .2)
            return self
        
pan = Product(30,"Pan", 2, "Black and Decker")
pan.displayInfo()
print(spc)
pan.return_item('opened')
pan.displayInfo()
print(spc)
googlehome = Product(150, "Google Home", 3, "Google")
googlehome.tax(.012)
googlehome.displayInfo()
print(spc)
googlehome.sell()
googlehome.displayInfo()
print(spc)
googlehome.return_item('defective')
googlehome.displayInfo()