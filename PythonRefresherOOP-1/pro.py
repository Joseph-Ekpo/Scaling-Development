# Task: Build a Car class with attributes (make, model) and method drive().
from lorem_text import lorem
import time

class Car:
   
    def __init__(self, make, model, starting_gas):
        self.make = make
        self.model = model
        self.fuel_capacity = starting_gas
        self.parked = True
    
    def __str__(self):
        return f"Make: {self.make}\nModel: {self.model}\nFuel: {self.fuel_capacity} gallons\nParked: {self.parked}"
    
    def drive(self, location):
        if self.parked:
            print("Cannot drive when parked. Start car first")
            return False
        else:
            print(f"Driving to: {location}. Consuming 1 fuel")
            self.fuel_capacity -= 1
            time.sleep(1)
            print(f"Arrived and parked at {location}..")
            self.parked = True
        return self.parked

    def park(self):
        self.parked = True
        return f"Parked the {self.make}in the cool shade!"
    
    def start_car(self):
        self.parked = False
        return f"{self.model} {self.make} is ready to rock-n-roll"
    
    def honk_horn(self):
        banter = "Can't you see I'm driving here!"
        noise = f"{lorem.words(5)}... " + banter
        return noise



honda = Car('Honda', 'civic', 12.56)
print(honda, "\n")

honda.start_car()
honda.drive("Los Angeles, CA")
print(honda, "\n")


print(honda.honk_horn())