class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"Vehicle Brand: {self.brand}, Year: {self.year}"



class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)   
        self.model = model

    
    def info(self):
        return f"Car Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
v = Vehicle("Toyota", 2010)
print(v.info())   


c = Car("Honda", 2022, "Civic")
print(c.info())