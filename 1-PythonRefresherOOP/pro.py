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



# honda = Car('Honda', 'civic', 12.56)
# print(honda, "\n")

# honda.start_car()
# honda.drive("Los Angeles, CA")
# print(honda, "\n")


# print(honda.honk_horn())


# Task: Check Validity of a String of Parentheses

class CheckValidity:
    open_flags = {
        '(':')',
        '{':'}',
        '[':']',
    }

    close_flags = {
        ')':'(',
        '}':'{',
        ']':'[]',
    }

    def __init__(self, pattern):
        self.pattern = list(pattern)
    
    def check_pattern(self):
        isValid = False

        # I will implement a stack using a list to check if the 'open' element has been 'closed'
        validator_stack = []

        # Check if we are starting with a valid sequence ie have we encountered an opening that needs closing: ( { [
        isOpen = False

        if len(self.pattern) < 2:
            return False
        elif self.pattern[0] in self.close_flags:
            return False
            # isOpen = self.pattern[0] in self.open_flags
            # print('open detected' if self.pattern[0] in self.open_flags else 'started closed')
        else:
            isOpen = True
            # {}(){}
            # {({})}
    
            for i in range(len(self.pattern)):
                if self.pattern[i] not in self.close_flags:
                    validator_stack.append(self.pattern[i])
                else:
                    if validator_stack.pop() != self.close_flags[self.pattern[i]]:
                        return False
                
            

        
        
        # At the end of iteration, the validator stack should be closed 
        # because there are no more open flags to close

        return len(validator_stack) == 0
    
# q1 = CheckValidity(r"()")
# print(f"{q1.check_pattern()}\t{True}")

# q2 = CheckValidity(r"(())")
# print(f"{q2.check_pattern()}\t{True}")

# q3 = CheckValidity(r"(()")
# print(f"{q3.check_pattern()}\t{False}")

# q4 = CheckValidity(r")(")
# print(f"{q4.check_pattern()}\t{False}")

# q5 = CheckValidity(r"((()))")
# print(f"{q5.check_pattern()}\t{True}")

# q6 = CheckValidity(r"(()())")
# print(f"{q6.check_pattern()}\t{True}")

q7 = CheckValidity(r"())(")
print(f"{q7.check_pattern()}\t{False}")

# q8 = CheckValidity(r"((())")
# print(f"{q8.check_pattern()}\t{False}")

# q9 = CheckValidity(r"()()()")
# print(f"{q9.check_pattern()}\t{True}")

# q10 = CheckValidity(r"(())()")
# print(f"{q10.check_pattern()}\t{True}")

# q11 = CheckValidity(r"(()))")
# print(f"{q11.check_pattern()}\t{False}")

# q12 = CheckValidity(r"((()()))")
# print(f"{q12.check_pattern()}\t{True}")

# q13 = CheckValidity(r"((()())")
# print(f"{q13.check_pattern()}\t{False}")

# q14 = CheckValidity(r")()(")
# print(f"{q14.check_pattern()}\t{False}")

# q15 = CheckValidity(r"((((()))))")
# print(f"{q15.check_pattern()}\t{True}")

# q16 = CheckValidity(r"(()(()))")
# print(f"{q16.check_pattern()}\t{True}")

# q17 = CheckValidity(r"()(()")
# print(f"{q17.check_pattern()}\t{False}")

# q18 = CheckValidity(r"")
# print(f"{q18.check_pattern()}\t{True}")  # empty string is balanced

# q19 = CheckValidity(r"())")
# print(f"{q19.check_pattern()}\t{False}")

# q20 = CheckValidity(r"((())())")
# print(f"{q20.check_pattern()}\t{True}")
