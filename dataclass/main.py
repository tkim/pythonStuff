from dataclasses import dataclass, field

@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int = field(repr=False)
    cash: float = field(compare=True, default=0.00)

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("John", 80, 700000)
i2 = Investor("Adam", 40, 100000)
i3 = Investor("Mike", 44, 400000)


mylist = [i1, i2, i3]

print(i1)
print (i2)
print(i2 < i3)
print(mylist)
