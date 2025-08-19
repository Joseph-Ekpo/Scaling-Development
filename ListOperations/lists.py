class DeDuper:
    def __init__(self):
        self.operations = 0

    
    def remove_duplicates(self, element):
        self.operations += 1
        return set(element)
    

dd = DeDuper()
print(dd.remove_duplicates([1, 1, 4, 5, 7, 7, 4, 3, 2, 56, 7, 2, 4, 1]))
