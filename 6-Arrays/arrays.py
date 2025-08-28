# Write a class that has a method called max_profit(earning) and 
# provides the maximum earning.
import random

class ProfitCalculator:

    def __init__(self, reciept: str):
        self.reciept = reciept
        

    def max_profit(self, earnings: list) -> int:
        maximum = None
        
        for q in range(len(earnings)):
            if not maximum:
                maximum = earnings[q]
            elif earnings[q] > maximum:
                maximum = earnings[q]


        return maximum


account_rep = ProfitCalculator('r')

test_lists = [[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        test_lists[i][j] = random.randint(1, 300)

for i in range(len(test_lists)):
    pass
    print(test_lists[i])
    print(f"Max: {account_rep.max_profit(test_lists[i])}")
    
# print(account_rep.max_profit(earnings=[300, 500, 400]))

