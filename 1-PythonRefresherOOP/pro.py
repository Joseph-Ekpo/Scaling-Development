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
        balanced = False

        # I will implement a stack using a list to check if the 'open' element has been 'closed'
        validator_stack = []

        # Counter for the number of elements currently open
        checked = len(self.pattern)

        if len(self.pattern) == 0:
            balanced = True
        elif len(self.pattern) % 2 > 0:
            balanced = False
        elif self.pattern[0] in self.close_flags:
            balanced = False
            # isOpen = self.pattern[0] in self.open_flags
            # print('open detected' if self.pattern[0] in self.open_flags else 'started closed')
        else:
            # {}(){}
            # { ( { } ) }

            # 
            # 
            # 
    
            for i in range(len(self.pattern)):
                if self.pattern[i] not in self.close_flags:
                    validator_stack.append(self.pattern[i])
                    checked -= 1
                elif len(validator_stack) > 0 and checked > 0:
                        if validator_stack.pop() == self.close_flags[self.pattern[i]]:
                             checked -= 1
                else:
                    balanced = checked == 0
                    
        
        
        # At the end of iteration, the validator stack should be closed 
        # because there are no more open flags to close

        return balanced
    
q1 = CheckValidity(r"()")
print(f"1 {q1.check_pattern()}\t{True}")

q2 = CheckValidity(r"(())")
print(f"2 {q2.check_pattern()}\t{True}")

q3 = CheckValidity(r"(()")
print(f"3 {q3.check_pattern()}\t{False}")

q4 = CheckValidity(r")(")
print(f"4 {q4.check_pattern()}\t{False}")

q5 = CheckValidity(r"((()))")
print(f"5 {q5.check_pattern()}\t{True}")

q6 = CheckValidity(r"(()())")
print(f"6 {q6.check_pattern()}\t{True}")

q7 = CheckValidity(r"())(")
print(f"7 {q7.check_pattern()}\t{False}")

q8 = CheckValidity(r"((())")
print(f"8 {q8.check_pattern()}\t{False}")

q9 = CheckValidity(r"()()()")
print(f"9 {q9.check_pattern()}\t{True}")

q10 = CheckValidity(r"(())()")
print(f"10 {q10.check_pattern()}\t{True}")

q11 = CheckValidity(r"(()))")
print(f"11 {q11.check_pattern()}\t{False}")

q12 = CheckValidity(r"((()()))")
print(f"12 {q12.check_pattern()}\t{True}")

q13 = CheckValidity(r"((()())")
print(f"13 {q13.check_pattern()}\t{False}")

q14 = CheckValidity(r")()(")
print(f"14 {q14.check_pattern()}\t{False}")

q15 = CheckValidity(r"((((()))))")
print(f"15 {q15.check_pattern()}\t{True}")

q16 = CheckValidity(r"(()(()))")
print(f"16 {q16.check_pattern()}\t{True}")

q17 = CheckValidity(r"()(()")
print(f"17 {q17.check_pattern()}\t{False}")

q18 = CheckValidity(r"")
print(f"18 {q18.check_pattern()}\t{True}")  # empty string is balanced

q19 = CheckValidity(r"())")
print(f"19 {q19.check_pattern()}\t{False}")

q20 = CheckValidity(r"((())())")
print(f"20 {q20.check_pattern()}\t{True}")
