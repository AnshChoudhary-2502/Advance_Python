import datetime
class Car:                                                      # class
    def __init__(self, name, model,year):                       # constructor
        self.name = name                                        # attribute
        self.model = model
        self.year = year

    def age(self):
        Age = datetime.datetime.now().year - self.year
        return Age

car1 = Car("Creta", "S + Knight Edition", 2023)                 # object
car2 = Car("M4", "Comp", 2022)

print(car1.name)
print(car2.model)

car2.year = 2021
print(car2.year)

print(car2.age())