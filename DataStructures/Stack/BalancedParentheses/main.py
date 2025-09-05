# Complete the is_balanced function.

# It takes a string as input and returns True if the parentheses in the string are balanced, and False otherwise. 
# Use an instance of the provided Stack class in stack.py to keep track of the parentheses.

# Only consider the characters ( and ) for this challenge.
from stack import Stack


def is_balanced(input_str):
    
    str_stack = Stack()
    balanced = False
    if len(input_str) % 2 == 0:
        for item in input_str:
            if item == '(':
                str_stack.push(item)
            else:
                if str_stack.peek() != item:
                    str_stack.pop()
                else:
                    break

        if str_stack.size() == 0:
            balanced = True
    
    return balanced
