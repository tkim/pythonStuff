class Investor:

    def __init__(self, name: str, age: int, cash: float):
        self.name = name
        self.age = age
        self.cash = cash

    def __repr__(self):
        return f"Name: {self.name}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.cash < other.cash
    

i1 = Investor("John", 25, 9000)
i2 = Investor("Anna", 30, 12000)
i3 = Investor("Bob", 70, 800000)

print(i1)
print(i1 < i3)