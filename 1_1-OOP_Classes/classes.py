# R-2.7
#  Write a Python class, Flower, that has three instance variables of type str, int, and float, 
# that respectively represent the name of the flower, its number of petals, and its price. 

# Your class must include a constructor method that initializes each variable to an appropriate value, 
# and your class should include methods for setting the value of each type, and retrieving the value of each type.

# Pseudo UML
# Flower
# fields: _name:str, _number_of_petals:int, _price:float
# behaviours: get/set(_name), get/set(_number_of_petals), get/set(_price)

class Flower:
    
    def __init__(self, name, number_of_petals, price):
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price
    
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number_of_petals(self):
        return self._number_of_petals

    def set_number_of_petals(self, number_of_petals):
        self._number_of_petals = number_of_petals

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

standard_bouquet = [
    Flower('Rose', 5, 3.50), 
    Flower('Violet', 6, 2.35), 
    Flower('Dandelion', 50, 25.50)
    ]

total = 0.0
# print(f"Bouquet price before savings{sum(individual_flower_cost) for }")
for flower in standard_bouquet:
    total += flower.get_price()
# print(f"Bouquet price before savings: ${total}")

total = 0.0
# Customer gets discount on a standard bouquet
for flower in standard_bouquet:
    flower.set_price(flower.get_price() * .5)
    total += flower.get_price()

# print(f"Bouquet price after savings: ${total}")

# R-2.9
# Implement the sub method for the Vector class of Section 2.3.3, 
# so that the expression u−v returns a new vector instance representing the difference between two vectors.
import random
class Vector:
# ”””Represent a vector in a multidimensional space.”””
    def __init__(self, d):
        self.coords = [0] * d


    def __len__(self): return len(self.coords)
    

    def __getitem__(self, j): return self.coords[j]


    def __setitem__(self, j, val): self.coords[j] = val


    def __eq__(self, other): return self. coords == other. coords


    def __ne__(self, other): return not self == other # rely on existing     eq     definition


    def __str__(self): return   f"<{str(self.coords)[1:-1]}>"


    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self)) 
        
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        
        return result
    

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))

        for i in range(len(self)):
            result[i] = self[i] - other[i]
        
        return result
 

u = Vector(4)
v = Vector(4)

for i in range(4):
    u[i] = random.randint(1, 50)
    v[i] = random.randint(1, 50)
    

print(f"Vector U: {u}")
print(f"Vector V: {v}")
print()
print(f"Vector U + V = {u + v}")
print(f"Vector U - V = {u - v}")

