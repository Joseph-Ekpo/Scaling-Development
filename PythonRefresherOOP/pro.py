# Leet Code 1: Two Sum

# Task: Build a Car class with attributes (make, model) and method drive().
 # car sizes -->
    # small = 1
    # medium = 2
    # big = 3
    # 

class ParkingLot:
    
    def __init__(self, spaces):
        # spaces --> [small, medium, big]
        self.spaces = spaces


class Car:
   
    def __init__(self, make, model, size):
        self.make = make
        self.model = model
        self.size = size
    
    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\n Size: {self.size}"
    
    def drive(self):
        pass

    def park(self, lot) --> bool:
        pass


honda = Car('honda', 'civic', 1)

